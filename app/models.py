from datetime import datetime

from .database import db


class URL(db.Model):
    __tablename__ = "urls"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    original_url = db.Column(
        db.String(2048),
        nullable=False
    )

    short_code = db.Column(
        db.String(10),
        unique=True,
        nullable=False,
        index=True
    )

    click_count = db.Column(
        db.Integer,
        default=0,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    def to_dict(self, base_url):
        return {
            "id": self.id,
            "original_url": self.original_url,
            "short_code": self.short_code,
            "short_url": f"{base_url}/{self.short_code}",
            "click_count": self.click_count,
            "created_at": self.created_at.isoformat()
        }