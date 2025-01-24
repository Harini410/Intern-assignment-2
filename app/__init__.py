from flask import Flask
from .routes import main as main_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    app.register_blueprint(main_routes)

    return app