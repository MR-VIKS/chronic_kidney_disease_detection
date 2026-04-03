from flask import Flask

def create_app():
    """Factory builder for the Flask Application"""
    app = Flask(__name__)

    # Import and register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
