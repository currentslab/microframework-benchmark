from microframeworks.settings import HOST, PORT, JSON_DATA, TEXT
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/about")
def about():
    return "Flask"

@app.route("/json")
def json_test():
    return jsonify(JSON_DATA)

@app.route("/text")
def text_test():
    return TEXT
