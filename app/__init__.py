from flask import Flask, request
from flask_cors import CORS
from app.blueprint import Blueprint
from app.config import ErrorHandler
from app.config.env import values
from app.utility.celery import celery_init_app
from app.utility.mail import MailHandler


def create_app():
    app = Flask(__name__, static_folder=None)
    CORS(app, resources={r"/*": {"origins": "*", "allow_headers": "*", "methods": "*"}})

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

    @app.before_request
    def handle_options_request():
        if request.method == "OPTIONS":
            response = app.make_default_options_response()
            headers = response.headers

            headers["Access-Control-Allow-Origin"] = "*"
            headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
            headers["Access-Control-Allow-Headers"] = "X-User-Language, Content-Type"

            return response

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add(
            "Access-Control-Allow-Headers",
            "X-User-Language, Content-Type, Authorization",
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"
        )
        return response

    return app
