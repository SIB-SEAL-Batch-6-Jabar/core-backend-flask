from flask import Flask
from flask_mail import Mail
from app.config.env import values
from app.utility.string import str_to_bool


class MailHandler:
    mail = Mail()

    @staticmethod
    def init(app: Flask):
        app.config["MAIL_SERVER"] = values["MAIL_SERVER"]
        app.config["MAIL_PORT"] = int(values["MAIL_PORT"])
        app.config["MAIL_USERNAME"] = values["MAIL_USERNAME"]
        app.config["MAIL_PASSWORD"] = values["MAIL_PASSWORD"]
        app.config["MAIL_USE_TLS"] = str_to_bool(values["MAIL_USE_TLS"])
        app.config["MAIL_USE_SSL"] = str_to_bool(values["MAIL_USE_SSL"])
        app.config["MAIL_DEFAULT_SENDER"] = values["MAIL_FROM_NAME"]
        return MailHandler.mail.init_app(app)

    @staticmethod
    def send(msg):
        return MailHandler.mail.send(msg)
