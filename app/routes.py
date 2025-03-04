from flask import Blueprint

def init_routes(app):
    main_bp = Blueprint('main', __name__)

    @main_bp.route('/')
    def home():
        return "Hello, Flask!"

    app.register_blueprint(main_bp)
