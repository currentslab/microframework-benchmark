from aiohttp import web
from microframeworks.settings import HOST, PORT, JSON_DATA, TEXT
import ujson
import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))

def text_test(request):
    return web.Response(text=TEXT)

def json_test(request):
    return web.Response(text=ujson.dumps(JSON_DATA), content_type='application/json')

def about(request):
    return web.Response(text='Aiohttp')

app = web.Application()
app.router.add_get(path='/about', handler=about, name='about')
app.router.add_get(path='/json', handler=json_test, name='json')
app.router.add_get(path='/text', handler=text_test, name='text')

if __name__ == "__main__":
    web.run_app(app, host=HOST, port=PORT)

