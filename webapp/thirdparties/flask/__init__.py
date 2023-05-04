from flask import Flask, Blueprint
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .dataaccess import db
from .config import Config


bp = Blueprint('api', __name__)


def create_app(config=Config):
    app = Flask(__name__)
    CORS(app, expose_headers=["Content-Disposition"])
    app.config.from_object(config)
    JWTManager(app)
    db.connect(config.DB_URL)
    db.create_all(overwrite=True)  # TODO: stop clean db every deploy
    app.register_blueprint(bp, url_prefix='/')
    return app


from . import users, tokens  # noqa: 401