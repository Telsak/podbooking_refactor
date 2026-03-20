from flask import Flask
from myproject.config import Config
from .extensions import db, migrate
from .routes.main import main
from .routes.api import api

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)
    app.register_blueprint(api)

    return app