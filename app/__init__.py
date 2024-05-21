from flask import Flask
from app.blueprint import Blueprint
from app.config import ErrorHandler


def create_app():
    app = Flask(__name__, static_folder=None)

    ErrorHandler.registerErrorHandler(app)
    Blueprint.register(app)

    return app