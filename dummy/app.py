from pathlib import Path

from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy


# -------- App+Db --------
def db_instance(app):
    db_path = Path(__file__).parent / "../www/dummy.db"
    return SQLAlchemy(app)


def create_app(name, config):
    app = Flask(name)
    app.config.update(config.db_config)
    return app


# -------- Models --------
class Asset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creation_date = db.Column(db.DateTime())
    asset = db.Column(db.Text())


# -------- Views --------
@app.route()
def foo(tag):
    return request.host_url, 200
