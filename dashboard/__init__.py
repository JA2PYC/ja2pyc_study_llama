from flask import Flask

# 블루프린트 가져오기
from dashboard.routes.home import home_bp
from dashboard.routes.api import api_bp
from dashboard.routes.model import model_bp
from dashboard.routes.static import static_bp

# Flask 앱 생성 및 블루프린트 등록
def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(home_bp)
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(model_bp, url_prefix="/model")
    app.register_blueprint(static_bp, url_prefix="/static")

    return app
