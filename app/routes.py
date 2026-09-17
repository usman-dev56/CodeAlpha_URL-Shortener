import random
import string

import validators
from flask import Blueprint, jsonify, redirect, request

from .database import db
from .models import URL


url_routes = Blueprint(
    "url_routes",
    __name__
)


def generate_short_code(length=6):
    """
    Generate a unique random short code.
    """

    characters = (
        string.ascii_letters +
        string.digits
    )

    while True:
        short_code = "".join(
            random.choices(
                characters,
                k=length
            )
        )

        existing_url = URL.query.filter_by(
            short_code=short_code
        ).first()

        if not existing_url:
            return short_code


@url_routes.route("/", methods=["GET"])
def home():
    """
    Basic API health check.
    """

    return jsonify({
        "message": "CodeAlpha URL Shortener API is running",
        "status": "success"
    }), 200


@url_routes.route(
    "/api/shorten",
    methods=["POST"]
)
def shorten_url():
    """
    Create a shortened URL.
    """

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Request body is required"
        }), 400

    if "url" not in data:
        return jsonify({
            "error": "URL is required"
        }), 400

    original_url = data["url"].strip()

    if not original_url:
        return jsonify({
            "error": "URL cannot be empty"
        }), 400

    if not validators.url(original_url):
        return jsonify({
            "error": (
                "Invalid URL. "
                "Please provide a valid URL."
            )
        }), 400

    existing_url = URL.query.filter_by(
        original_url=original_url
    ).first()

    if existing_url:
        return jsonify({
            "message": "URL already shortened",
            **existing_url.to_dict(
                request.host_url.rstrip("/")
            )
        }), 200

    short_code = generate_short_code()

    new_url = URL(
        original_url=original_url,
        short_code=short_code
    )

    db.session.add(new_url)
    db.session.commit()

    return jsonify({
        "message": "URL shortened successfully",
        **new_url.to_dict(
            request.host_url.rstrip("/")
        )
    }), 201


@url_routes.route(
    "/<short_code>",
    methods=["GET"]
)
def redirect_to_original(short_code):
    """
    Redirect a short URL to the original URL.
    """

    url = URL.query.filter_by(
        short_code=short_code
    ).first()

    if not url:
        return jsonify({
            "error": "Short URL not found"
        }), 404

    url.click_count += 1

    db.session.commit()

    return redirect(
        url.original_url
    )


@url_routes.route(
    "/api/urls/<short_code>",
    methods=["GET"]
)
def get_url_details(short_code):
    """
    Get information about a shortened URL.
    """

    url = URL.query.filter_by(
        short_code=short_code
    ).first()

    if not url:
        return jsonify({
            "error": "Short URL not found"
        }), 404

    return jsonify(
        url.to_dict(
            request.host_url.rstrip("/")
        )
    ), 200


@url_routes.route(
    "/api/urls/<short_code>",
    methods=["DELETE"]
)
def delete_url(short_code):
    """
    Delete a shortened URL.
    """

    url = URL.query.filter_by(
        short_code=short_code
    ).first()

    if not url:
        return jsonify({
            "error": "Short URL not found"
        }), 404

    db.session.delete(url)

    db.session.commit()

    return jsonify({
        "message": "Short URL deleted successfully"
    }), 200