import os
from flask import render_template
from flask_mail import Message
import joblib
from celery import shared_task
from app.config.http import ExceptionHandler
from app.utility.mail import MailHandler


@shared_task()
def calculate(email, data):
    try:
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

        model = joblib.load(os.path.join(ROOT_DIR, "../data/random_forest.joblib"))
        prediction = model.predict([list(data.values())])

        match prediction[0]:
            case 0:
                result = "No Diabetes"
            case 1:
                result = "Pre-Diabetes"
            case 2:
                result = "Diabetes"

        msg = Message(
            subject="SiManis: Diabetes Result",
            recipients=[email],
            sender=("SiManis", "noreply@morningstarlibrary.com"),
            html=render_template("result.html", result=result),
        )

        MailHandler.send(msg)

        return f"Success! Result has been sent to {email}"
    except ExceptionHandler as e:
        print(e)
