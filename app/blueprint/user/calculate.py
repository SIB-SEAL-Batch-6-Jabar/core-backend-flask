import os
from flask import Blueprint, request
import joblib

from app.config.http import ExceptionHandler, HTTPResponse

from app.validator import validator
from app.validator.user import UserValidator

CalculateBlueprint = Blueprint("calculate", __name__, url_prefix="/calculate")


@CalculateBlueprint.route("/", methods=["POST"])
@validator(UserValidator.CalculateForm)
def calculate(body):
    try:
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

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
        print(data)

        model = joblib.load(os.path.join(ROOT_DIR, "../../data/random_forest.joblib"))
        prediction = model.predict([list(data.values())])

        match prediction[0]:
            case 0:
                result = "No Diabetes"
            case 1:
                result = "Pre-Diabetes"
            case 2:
                result = "Diabetes"

        return HTTPResponse.success("Success calculating!", {"result": result})
    except ExceptionHandler as e:
        return HTTPResponse.error(e.message, e.data, e.status)
