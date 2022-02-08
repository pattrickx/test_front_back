from flask import Flask, request
from flask_cors import CORS


def create_app(testing: bool = True):
    app = Flask(__name__)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    @app.route("/hello")
    def test():
        return f"HELLO"

    return app