import uvicorn
from microframeworks.settings import HOST, PORT, JSON_DATA, TEXT
from starlette.applications import Starlette
from starlette.responses import UJSONResponse, Response
import uvicorn
import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

app = Starlette()

@app.route("/about")
async def service_name(request):
    return Response("Sanic")

@app.route("/json")
async def json_test(request):
    return UJSONResponse(JSON_DATA)

@app.route("/text")
async def text_test(request):
    return Response(TEXT)


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
