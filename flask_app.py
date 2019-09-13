# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, json, send_from_directory
import werkzeug
import werkzeug.exceptions

app = Flask(__name__)

# Intercepts generic server errors and logs them
@app.errorhandler(werkzeug.exceptions.HTTPException)
def handle_errors(e):
    logging.error(str(e))
    return str(e), 500

@app.route('/')
def hello_world():
    try:
        return render_template('base.html')
    except Exception as e:
        return str(e)
