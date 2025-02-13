from flask import Blueprint, jsonify
from models.predict import simple_predict

model_bp = Blueprint("model", __name__)

@model_bp.route("/predict")
def predict():
    result = simple_predict([1.0, 2.0, 3.0])
    return jsonify({"prediction": result})
