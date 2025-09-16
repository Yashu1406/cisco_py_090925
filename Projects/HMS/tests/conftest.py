import pytest
from app import create_app
from app.config import Config
from app.db import db
import tempfile
import os


class TestConfig(Config):
    TESTING = True
    DB_PATH = os.path.join(tempfile.gettempdir(), "hms_test.sqlite")
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_PATH}"
    SMTP_HOST = "localhost"
    SMTP_PORT = 1025  # test server if needed


@pytest.fixture
def app():
    app = create_app(TestConfig())
    with app.app_context():
        db.drop_all()
        db.create_all()
        yield app
    # clean
    try:
        os.remove(TestConfig.DB_PATH)
    except Exception:
        pass


@pytest.fixture
def client(app):
    return app.test_client()
