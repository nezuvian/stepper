from flask import (Flask, render_template, jsonify)
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/jquery")
def jquery():
    data = {"text": "asdfasdfa"}
    return jsonify(data)