import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "dev-secret-key"
    )

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///urls.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BASE_URL = os.getenv(
        "BASE_URL",
        "http://127.0.0.1:5000"
    )