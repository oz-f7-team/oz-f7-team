from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app)
    Migrate(app, db)

    from .routes import api_bp
    app.register_blueprint(api_bp)

    return app
