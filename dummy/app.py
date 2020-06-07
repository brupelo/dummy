from pathlib import Path

from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(name, config):
    app = Flask(name)
    app.config.update(config.db_config)
    db.init_app(app)
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
