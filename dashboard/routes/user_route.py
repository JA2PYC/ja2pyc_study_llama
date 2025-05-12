# dashboard/route/user_route.py
from flask import Blueprint, jsonify
from database.services.user_service import UserService

user_bp = Blueprint("user", __name__, url_prefix="/users")
user_service = UserService()

@user_bp.route("/", methods=["GET"])
def get_users():
    users = user_service.list_users()
    result = [{"id": u.id, "name": u.name, "email": u.email} for u in users]
    return jsonify(result)

@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_service.get_user(user_id)
    if user:
        return jsonify({"id": user.id, "name": user.name, "email": user.email})
    return jsonify({"error": "User not found"}), 404
