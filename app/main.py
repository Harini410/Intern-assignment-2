from flask import Flask
from app.routes import chatbot_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    app.register_blueprint(chatbot_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
