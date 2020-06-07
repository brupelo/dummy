import logging
import os
from pathlib import Path


class ConfigBase(object):
    def __init__(self, db_path, debug=True):
        self.db_config = {
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{self.db_path}",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
        }
        self.debug = debug

        FLASK_ENV = os.environ.get("FLASK_ENV", "development")
        if FLASK_ENV == "development":
            logging.basicConfig(level=logging.DEBUG)
        elif FLASK_ENV == "production":
            logging.basicConfig(level=logging.INFO)
