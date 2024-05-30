from wtforms import EmailField, Form, FloatField
from wtforms.validators import NumberRange, AnyOf

from ..custom import Required


class CalculateForm(Form):
    Email = EmailField("Email", [Required()])
    HighBP = FloatField(
        "HighBP",
        [Required(), AnyOf([0, 1])],
    )
    HighChol = FloatField("HighChol", [Required(), AnyOf([0, 1])])
    CholCheck = FloatField("CholCheck", [Required(), AnyOf([0, 1])])
    BMI = FloatField("BMI", [Required(), NumberRange(min=1)])
    Smoker = FloatField("Smoker", [Required(), AnyOf([0, 1])])
    Stroke = FloatField("Stroke", [Required(), AnyOf([0, 1])])
    HeartDiseaseorAttack = FloatField(
        "HeartDiseaseorAttack", [Required(), AnyOf([0, 1])]
    )
    PhysActivity = FloatField("PhysActivity", [Required(), AnyOf([0, 1])])
    Fruits = FloatField("Fruits", [Required(), AnyOf([0, 1])])
    Veggies = FloatField("Veggies", [Required(), AnyOf([0, 1])])
    HvyAlcoholConsump = FloatField("HvyAlcoholConsump", [Required(), AnyOf([0, 1])])
    AnyHealthcare = FloatField("AnyHealthcare", [Required(), AnyOf([0, 1])])
    NoDocbcCost = FloatField("NoDocbcCost", [Required(), AnyOf([0, 1])])
    GenHlth = FloatField("GenHlth", [Required(), AnyOf([1, 2, 3, 4, 5])])
    MentHlth = FloatField("MentHlth", [Required(), NumberRange(min=0, max=30)])
    PhysHlth = FloatField("PhysHlth", [Required(), NumberRange(min=0, max=30)])
    DiffWalk = FloatField("DiffWalk", [Required(), AnyOf([0, 1])])
    Sex = FloatField("Sex", [Required(), AnyOf([0, 1])])
    Age = FloatField("Age", [Required(), NumberRange(min=1, max=13)])
