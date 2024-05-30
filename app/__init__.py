from flask import Flask
from flask_cors import CORS
from flask_mail import Mail
from app.blueprint import Blueprint
from app.config import ErrorHandler
from app.config.env import values
from app.utility.celery import celery_init_app
from app.utility.mail import MailHandler
from app.utility.string import str_to_bool


def create_app():
    app = Flask(__name__, static_folder=None)
    CORS(app, resources={r"/*": {"origins": "*"}})

    app.config.from_mapping(
        CELERY=dict(
            broker_url=values["REDIS_URL"],
            result_backend=values["REDIS_URL"],
            task_ignore_result=True,
        ),
    )
    app.config.from_prefixed_env()

    celery_init_app(app)

    MailHandler.init(app)
    ErrorHandler.registerErrorHandler(app)
    Blueprint.register(app)

    def after_request(response):
        header = response.headers
        header["Access-Control-Allow-Origin"] = "*"
        header["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        header["Access-Control-Allow-Methods"] = "OPTIONS, HEAD, GET, POST, DELETE, PUT"
        return response

    app.after_request(after_request)

    return app
