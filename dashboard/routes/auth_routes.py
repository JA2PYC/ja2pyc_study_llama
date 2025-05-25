# dashboard/routes/auth_routes.py

from flask import Blueprint, request, jsonify
from auth.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    token = AuthService.login(data["login_id"], data["password"])
    if not token:
        return jsonify({"error": "Invalid credentials"}), 401
    return jsonify({"access_token": token})
