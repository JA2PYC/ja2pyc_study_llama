from flask import Blueprint, jsonify, request
from api.external_api import get_external_data
import api.openai_api as openai_api

api_bp = Blueprint("api", __name__)

@api_bp.route("/data")
def fetch_data():
    data = get_external_data()
    return jsonify(data)

@api_bp.route("/chat_openai", methods = ['POST'])
def chat_openai():
    try:
        data = request.json
        messages = data.get("messages",[])
        model = data.get("model", "gpt-4")
        temperature = data.get("temperature", 0.7)
        
        if not messages:
            return jsonify({"error" : "Messages are required."}), 400
        
        response_text = openai_api.chatCompletion(messages,model,temperature)
        return jsonify({"response": response_text})
    
    except Exception as e:
        return jsonify({"error" : str(e)}), 500