from flask import Flask
from app.db import init_db
from app.models import Base
from app.routes import bp
from app.logger import logger

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)
    init_db(Base)
    logger.info("Application started and DB initialized")
    return app