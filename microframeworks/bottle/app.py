from bottle import route, run
from microframeworks.settings import HOST, PORT, JSON_DATA, TEXT

@route('/about')
def about():
    return "Bottle"

@route("/json")
def json_test():
    return JSON_DATA

@route("/text")
def text_test():
    return TEXT

if __name__ == "__main__":
    run(host=HOST, port=PORT, debug=False)
