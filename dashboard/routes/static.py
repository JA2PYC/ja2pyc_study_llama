from flask import Blueprint, send_from_directory
import os

static_bp = Blueprint("static", __name__)

@static_bp.route("/<path:filename>")
def static_filename(filename):
    return send_from_directory(os.path.join(os.getcwd(), 'node_modules/bootstrap-icons/font'), filename)
