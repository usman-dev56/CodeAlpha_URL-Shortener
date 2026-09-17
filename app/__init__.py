from flask import Flask

from config import Config
from .database import db


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    from .routes import url_routes

    app.register_blueprint(url_routes)

    with app.app_context():
        db.create_all()

    return app