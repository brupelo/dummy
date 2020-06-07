from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(domain_name):
    # TODO: Should follow OCP eventually, let's keep it simple for now though
    from dummy import ConfigDomain1, ConfigDomain2

    config = {"domain1": ConfigDomain1, "domain2": ConfigDomain2}[domain_name]()

    app = Flask()
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
