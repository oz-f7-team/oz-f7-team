from config import db
from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api

migrate = Migrate()

def create_app():
    application = Flask(__name__)    

    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    db.init_app(application)
    #create_app()에서 db.init_app(application)을 호출하여 SQLAlchemy를 Flask 앱과 연결.
    #Flask-Migrate를 사용하여 마이그레이션 관리.

    migrate.init_app(application, db)
    
    api = Api(application)
    
    from app.routes import user_bp, questions_bp, image_bp, choices_bp
    from app.stats_routes import stats_routes

    api.register_blueprint(stats_routes)
    api.register_blueprint(user_bp)
    api.register_blueprint(questions_bp)
    api.register_blueprint(image_bp)
    api.register_blueprint(choices_bp)
    
    return application