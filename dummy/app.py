from dummy.domain1.config import Config as ConfigDomain2
from flask import Flask, Blueprint
from flask import request

from dummy.views import main
from dummy.domain1.config import ConfigDomain1
from dummy.domain1.config import ConfigDomain2


def create_app(domain_name):
    print("======>", domain_name)
    # config = {"domain1": ConfigDomain1, "domain2": ConfigDomain2}[domain_name]()
    app = Flask(__name__)
    # app.config.update(config.db_config)
    # db.init_app(app)
    app.register_blueprint(main)
    return app
