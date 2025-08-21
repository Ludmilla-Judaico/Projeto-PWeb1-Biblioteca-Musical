from flask import Flask
from .main import app as app_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'segredinho'

    app.register_blueprint(app_bp)

    return app

