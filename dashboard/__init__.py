from flask import Flask

def create_app():
    print("Create App")

    app = Flask(__name__)

    from .dashboard import dashboard

    app.register_blueprint(dashboard)

    return app