from microframeworks.settings import HOST, PORT, JSON_DATA, TEXT
from flask import Flask, jsonify
import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

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

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=False)