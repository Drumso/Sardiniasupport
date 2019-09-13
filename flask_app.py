# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request, json, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        return render_template('base.html')
    except Exception as e:
        return str(e)
