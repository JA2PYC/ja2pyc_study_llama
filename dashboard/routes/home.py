from flask import Blueprint, render_template, request, jsonify
from dashboard.tasks import test_task

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    return render_template("index.html")

@home_bp.route("test_task")
def start_task():
    seconds = int(request.args.get('sec', 5))
    task = test_task.long_task(seconds)
    return jsonify({"task_id" : task.id})
