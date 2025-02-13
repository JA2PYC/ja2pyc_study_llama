from flask import Blueprint, jsonify
from api.external_api import get_external_data

api_bp = Blueprint("api", __name__)

@api_bp.route("/data")
def fetch_data():
    data = get_external_data()
    return jsonify(data)
