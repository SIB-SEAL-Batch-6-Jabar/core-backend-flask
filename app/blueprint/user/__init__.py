from flask import Blueprint
from .calculate import CalculateBlueprint

UserBlueprint = Blueprint("user", __name__, url_prefix="/")

UserBlueprint.register_blueprint(CalculateBlueprint)
