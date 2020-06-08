import logging
import os
from pathlib import Path

from flask import Blueprint
from flask import Flask
from flask import current_app
from flask_sqlalchemy import SQLAlchemy


# -------- Configs --------
class Config(object):
    def __init__(self, db_path, debug=True):
        self.db_config = {
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_path}",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
        self.debug = debug

        FLASK_ENV = os.environ.get("FLASK_ENV", "development")
        if FLASK_ENV == "development":
            logging.basicConfig(level=logging.DEBUG)
        elif FLASK_ENV == "production":
            logging.basicConfig(level=logging.INFO)


class Domain1(Config):
    def __init__(self, debug=True):
        db_path = Path(__file__).parent / "../../www/domain1.db"
        super().__init__(db_path, debug=debug)
        self.domain_config = {"test": "domain1_test"}


class Domain2(Config):
    def __init__(self, debug=True):
        db_path = Path(__file__).parent / "../../www/domain2.db"
        super().__init__(db_path, debug=debug)
        self.domain_config = {"test": "domain2_test"}


# -------- Models --------
db = SQLAlchemy()


class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime())
    asset = db.Column(db.Text())


# -------- Views --------
main = Blueprint("main", __name__)


@main.route("/")
def main_index():
    cfg = current_app.domain_config
    return f"This is {cfg['test']}"


# -------- App --------
def create_app():
    domain = os.environ.get("DOMAIN", "domain1")
    app = Flask(__name__)
    config = {"domain1": Domain1(), "domain2": Domain2()}[domain]
    app.config.update(config.db_config)
    app.domain_config = config.domain_config
    db.init_app(app)
    app.register_blueprint(main)
    return app
