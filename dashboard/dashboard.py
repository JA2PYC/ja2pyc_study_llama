from flask import Blueprint, render_template, request, jsonify

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/")
def dashboard_route():
    return render_template("dashboard.html")