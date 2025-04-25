from flask import Blueprint, render_template, request, jsonify
from dashboard.tasks.test_task import long_task

# Celery Hint
# from celery import Task
# long_task: Task

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    return render_template("index.html")

@home_bp.route("test_task")
def start_task():
    seconds = int(request.args.get('sec', 5))
    # task = long_task.apply_async(args=[5], countdown=10)
    task = long_task.delay(seconds)
    return jsonify({"task_id" : task.id})
