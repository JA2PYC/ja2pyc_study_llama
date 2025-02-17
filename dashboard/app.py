from dashboard import create_app

app = create_app()  # Flask 앱 생성

if __name__ == "__main__":
    app.run(debug=True)

# print("app.py / sys.path : ",sys.path)

# # import sys
# # import os
# # import logging
# # from flask import Flask

# # logging.basicConfig(
# #     filename="flask_env.log",
# #     level=logging.INFO,
# #     format="%(asctime)s - %(levelname)s - %(message)s"
# # )

# # app = Flask(__name__)

# # @app.route("/")
# # def routeHome():
# #     env_info = f"Python Executable: {sys.executable}\nVirtual Environment: {sys.prefix}\n"
# #     logging.info(env_info)
# #     return f"Running in virtual environment: {sys.prefix}"

# # if __name__ == "__main__":
# #     print (f"Flask Python Executable: {sys.executable}")
# #     print (f"Flask Virtual Environment: {sys.prefix}")
# #     print (f"Flask PID: {os.getpid()}")
# #     logging.info("Starting Flask Application...")
# #     app.run(debug=True, host="0.0.0.0", port= 5000)
