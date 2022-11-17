from flask import Flask
from flask_cors import CORS

from .routes import routes

def create_app():
    app = Flask(__name__)
    app.secret_key = "arael034"

    app.register_blueprint(routes, url_prefix="/")

    CORS(app)
    return app
