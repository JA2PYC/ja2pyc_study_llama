import requests

def get_external_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
        return response.json()
    except Exception as e:
        return {"error": str(e)}
