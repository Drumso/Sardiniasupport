# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    try:
        return render_template('base.html')
    except Error as e:
        return str(e)
