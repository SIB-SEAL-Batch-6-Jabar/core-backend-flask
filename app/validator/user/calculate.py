from wtforms import Form, FloatField, IntegerField


class CalculateForm(Form):
    HighBP = FloatField("HighBP")
    HighChol = FloatField("HighChol")
    CholCheck = FloatField("CholCheck")
    BMI = FloatField("BMI")
    Smoker = FloatField("Smoker")
    Stroke = FloatField("Stroke")
    HeartDiseaseorAttack = FloatField("HeartDiseaseorAttack")
    PhysActivity = FloatField("PhysActivity")
    Fruits = FloatField("Fruits")
    Veggies = FloatField("Veggies")
    HvyAlcoholConsump = FloatField("HvyAlcoholConsump")
    AnyHealthcare = FloatField("AnyHealthcare")
    NoDocbcCost = FloatField("NoDocbcCost")
    GenHlth = FloatField("GenHlth")
    MentHlth = FloatField("MentHlth")
    PhysHlth = FloatField("PhysHlth")
    DiffWalk = FloatField("DiffWalk")
    Sex = FloatField("Sex")
    Age = FloatField("Age")
