from flask import Flask, render_template
from .main import app as app_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'segredinho'

    app.register_blueprint(app_bp)
    
    @app.errorhandler(404)
    def not_found(err):
        return render_template("erros/404.html"), 404
    
    @app.errorhandler(405)
    def method_not_allowed(err):
        return render_template("erros/405.html"), 405
    
    @app.errorhandler(500)
    def erro_interno(err):
        return render_template("erros/500.html"), 500

    @app.errorhandler(502)
    def getway_invalido(err):
        return render_template("erros/502.html"), 502

    @app.errorhandler(400)
    def req_invalida(err):
        return render_template("erros/400.html"), 400
    return app
