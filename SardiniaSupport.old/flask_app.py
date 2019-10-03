# A very simple Flask Hello World app for you to get started with...
import os
import logging

from flask import Flask, render_template, request, json, send_from_directory
import werkzeug
import werkzeug.exceptions

import subprocess

# Test upload tre
try:
    repo_dir = os.path.join(os.getcwd(), "Sardiniasupport")
    git_result = subprocess.run(["git", "pull"], cwd=repo_dir)
except Exception as e:
    git_result = str(e)
    print(e)


def create_app():
    """Application factory function.

    This function generates the app instance of the backend and is useful to  assure that only one instance exists.

    It also retrieves settings from the configuration files to apply them to the application and contains the
    functions related to the different API calls.

    Returns
    -------
    app instance

    """
    
    app = Flask(__name__)
    app.debug = True

    # Intercepts generic server errors and logs them
    @app.errorhandler(werkzeug.exceptions.HTTPException)
    def handle_errors(e):
    #     logging.error(str(e))
        return str(e), 500

    # Main page
    @app.route('/')
    def default():
        try:
            return render_template('default.html', data=str(git_result))  # + "\n" + str(git_result.stdout) + "\n" + str(git_result.stderr))
        except Exception as e:
            return "Exception: " + str(e)

    @app.route('/recipe/<recipe_name>/')
    def recipes_pages(recipe_name):
        return str(recipe_name)
   
    # End of recipes function: 'create_app'
    return app
