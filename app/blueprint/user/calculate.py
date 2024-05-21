import os
from flask import Blueprint, render_template, request
from sklearn.ensemble import RandomForestClassifier
import joblib

from app.config.http import HTTPResponse

from ...validator.user import UserValidator

CalculateBlueprint = Blueprint("calculate", __name__, url_prefix="/calculate")


@CalculateBlueprint.route("/", methods=["POST"])
def calculate():
    try:
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        form = UserValidator.CalculateForm(data=request.json)

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

        if not form.validate():
            return HTTPResponse.error("Invalid form data!", form, 422)

        data = {column: form.data[column] for column in columns}
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

        # return HTTPResponse.success("Success calculating!", {"result": result})
        return model
    except Exception as e:
        return HTTPResponse.error(str(e), code="500")
