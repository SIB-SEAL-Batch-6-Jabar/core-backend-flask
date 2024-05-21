from wtforms import Form, FloatField
from wtforms.validators import NumberRange, AnyOf

from ..custom import Required


class CalculateForm(Form):
    HighBP = FloatField(
        "HighBP",
        [Required(), AnyOf([0.0, 1.0])],
    )
    HighChol = FloatField("HighChol", [Required(), AnyOf([0.0, 1.0])])
    CholCheck = FloatField("CholCheck", [Required(), AnyOf([0.0, 1.0])])
    BMI = FloatField("BMI", [Required(), NumberRange(min=1.0)])
    Smoker = FloatField("Smoker", [Required(), AnyOf([0.0, 1.0])])
    Stroke = FloatField("Stroke", [Required(), AnyOf([0.0, 1.0])])
    HeartDiseaseorAttack = FloatField(
        "HeartDiseaseorAttack", [Required(), AnyOf([0.0, 1.0])]
    )
    PhysActivity = FloatField("PhysActivity", [Required(), AnyOf([0.0, 1.0])])
    Fruits = FloatField("Fruits", [Required(), AnyOf([0.0, 1.0])])
    Veggies = FloatField("Veggies", [Required(), AnyOf([0.0, 1.0])])
    HvyAlcoholConsump = FloatField("HvyAlcoholConsump", [Required(), AnyOf([0.0, 1.0])])
    AnyHealthcare = FloatField("AnyHealthcare", [Required(), AnyOf([0.0, 1.0])])
    NoDocbcCost = FloatField("NoDocbcCost", [Required(), AnyOf([0.0, 1.0])])
    GenHlth = FloatField("GenHlth", [Required(), AnyOf([1.0, 2.0, 3.0, 4.0, 5.0])])
    MentHlth = FloatField("MentHlth", [Required(), NumberRange(min=1.0, max=30.0)])
    PhysHlth = FloatField("PhysHlth", [Required(), NumberRange(min=1.0, max=30.0)])
    DiffWalk = FloatField("DiffWalk", [Required(), AnyOf([0.0, 1.0])])
    Sex = FloatField("Sex", [Required(), AnyOf([0.0, 1.0])])
    Age = FloatField("Age", [Required(), NumberRange(min=1.0, max=13.0)])
