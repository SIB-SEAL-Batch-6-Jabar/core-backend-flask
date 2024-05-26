from flask import Blueprint

from app.config.http import ExceptionHandler, HTTPResponse

from app.tasks.calculate import calculate
from app.validator import validator
from app.validator.user import UserValidator

CalculateBlueprint = Blueprint("calculate", __name__, url_prefix="/calculate")


@CalculateBlueprint.route("/", methods=["POST"])
@validator(UserValidator.CalculateForm)
def execute(body):
    try:
        columns = [
            "HighBP",
            "HighChol",
            "CholCheck",
            "BMI",
            "Smoker",
            "Stroke",
            "HeartDiseaseorAttack",
            "PhysActivity",
            "Fruits",
            "Veggies",
            "HvyAlcoholConsump",
            "AnyHealthcare",
            "NoDocbcCost",
            "GenHlth",
            "MentHlth",
            "PhysHlth",
            "DiffWalk",
            "Sex",
            "Age",
        ]

        data = {column: body[column] for column in columns}

        result = calculate.delay(body["Email"], data)

        return HTTPResponse.success(
            "Success! Result will be sent to your email", result.id
        )
    except ExceptionHandler as e:
        return HTTPResponse.error(e.message, e.data, e.status)
