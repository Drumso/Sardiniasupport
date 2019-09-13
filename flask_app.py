# A very simple Flask Hello World app for you to get started with...
import os
import logging

from flask import Flask, render_template, request, json, send_from_directory
import werkzeug
import werkzeug.exceptions

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

    # Intercepts generic server errors and logs them
    @app.errorhandler(werkzeug.exceptions.HTTPException)
    def handle_errors(e):
    #     logging.error(str(e))
        return str(e), 500

    # Main page
    @app.route('/')
    def default():
        try:
            return render_template('default.html')
        except Exception as e:
            return str(e)
   
    # End of main function: 'create_app'
    return app
    
