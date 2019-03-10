from sanic import Sanic
from sanic import response
from datetime import datetime
from sanic.response import text, json
from microframeworks.settings import HOST, PORT, JSON_DATA, TEXT
import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

app = Sanic(__name__)


@app.route("/about")
async def service_name(request):
    return text("Sanic")

@app.route("/json")
async def json_test(request):
    return json(JSON_DATA)

@app.route("/text")
async def text_test(request):
    return text(TEXT)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=False)