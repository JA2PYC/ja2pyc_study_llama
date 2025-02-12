import os
import sys
import subprocess


print("Main", sys.executable)

def create_virtualenv():
    """Create a virtual environment if it doesn't exist."""
    if not os.path.exists("venv"):
        print("Creating a virtual environment...")
        try:
            subprocess.run(["python", "-m", "venv", "venv"], check=True)
            print("Successfully created virtual environment.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to create a virtual environment: {e}")
            sys.exit(1)


def activate_virtualenv():
    """Ensure the script runs inside the virtual environment."""
    venv_python = os.path.join(
        "venv", "Scripts" if os.name == "nt" else "bin", "python"
    )
    print("VENV", sys.executable)
    if sys.executable != os.path.abspath(venv_python):
        print("Restarting script inside the virtual environment...")
        print("Subprocess", sys.executable)
        subprocess.run([venv_python] + sys.argv)
        # sys.exit(0)


def install_dependencies():
    """Install dependencies from requirements.txt."""
    requirements_file = "requirements.txt"
    if not os.path.exists(requirements_file) or os.path.getsize(requirements_file) == 0:
        print(
            "Skipping dependency installation (no requirements.txt or file is empty)."
        )
        return

    print("Installing dependencies...")
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "--upgrade", "pip"], check=True
        )
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", requirements_file],
            check=True,
        )
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)


def run_flask_app():
    """Run the Flask application."""
    try:
        from dashboard import create_app

        print("Creating Flask app...")
        app = create_app()
        app.run(debug=True)
    except ImportError as e:
        print(f"Flask App Import Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Flask App Exception: {e}")
        sys.exit(1)


def main():
    create_virtualenv()
    print("Create", sys.executable)
    activate_virtualenv()
    print("Activate", sys.executable)
    install_dependencies()
    run_flask_app()


if __name__ == "__main__":
    if "FLASK_RUN_FROM_CLI" not in os.environ:
        main()

# import os
# import sys
# import subprocess

# # Create Virtual Environment.
# def create_virtualenv():
#     """Create a virtual environment."""
#     if not os.path.exists("venv"):
#         print("Creating a virtual environment...")
#         try:
#             subprocess.run(["python", "-m", "venv", "venv"], check=True)
#             print("Successfully created virtual environment.")
#         except subprocess.CalledProcessError as e:
#             print(f"Failed to create a virtual environment : {e}")
#             sys.exit(1)
#         except Exception as e:
#             print(f"Failed to create a virtual environment : {e}")
#             sys.exit(1)


# def activate_virtualenv():
#     """Activate a virtual environment."""
#     if os.environ.get("VIRTUAL_ENV"):
#         print("Virtual environment is already activated.")
#         return

#     venv_python = os.path.join(
#         "venv", "Scripts" if os.name == "nt" else "bin", "python"
#     )
#     activate_script = os.path.join(
#         "venv", "Scripts" if os.name == "nt" else "bin", "activate"
#     )
#     if not os.path.exists(activate_script):
#         print("Cannot find a venv script.")
#         sys.exit(1)

#     if sys.executable != os.path.abspath(venv_python):
#         os.environ["VIRTUAL_ENV"] = os.path.abspath("venv")
#         os.environ["PATH"] = os.path.join("venv", "bin") + os.pathsep + os.environ["PATH"]
#         print("Restart script inside the virtual environment.")
#         os.execv(venv_python, [venv_python] + sys.argv)
#     print("Activate a virtual environment.")


# def install_dependencies():
#     """Install Dependencies.."""
#     if os.environ.get("DEPENDENCIES_CHECKED"):
#         print("Already checked dependencies.")
#         return
#     requirements_file = "requirements.txt"
#     if not os.path.exists(requirements_file):
#         print("Cannot find a requirements.txt. Skip install dependenceis.")
#         return

#     if os.path.getsize(requirements_file) == 0:
#         print("File is empty. Skip install dependencies.")
#         return

#     print("Install dependencies.")
#     try:
#         subprocess.check_call(
#             [sys.executable, "-m", "pip", "install", "--upgrade", "pip"]
#         )
#         subprocess.check_call(
#             [sys.executable, "-m", "pip", "install", "-r", requirements_file]
#         )
#         os.environ["DEPENDENCIES_CHECKED"] = "true"
#         print("Complete install dependencies.")
#     except Exception as e:
#         print(f"Failed to install dependencies : {e}")
#         sys.exit(1)


# def run_flask_app():
#     """Run main"""
#     try:
#         from dashboard import create_app

#         print("Create flask app")
#         app = create_app()

#         app.run(debug=True)
#     except ImportError as e:
#         print(f"Flask App Import Error : {e}")
#         sys.exit(1)
#     except Exception as e:
#         print(f"Flask App Exception : {e}")
#         sys.exit(1)


# def main():
#     create_virtualenv()
#     activate_virtualenv()
#     install_dependencies()
#     run_flask_app()


# if __name__ == "__main__":
#     if "FLASK_RUN_FROM_CLI" not in os.environ:
#         main()
