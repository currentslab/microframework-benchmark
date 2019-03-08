from japronto import Application
import ujson
from microframeworks.settings import HOST, PORT, JSON_DATA, TEXT

def text_test(request):
    return request.Response(text=TEXT)

def json_test(request):
    return request.Response(text=ujson(JSON_DATA), mime_type='application/json')

def about(request):
    return request.Response(text='Sanic')

if __name__ == "__main__":    
    app = Application(debug=False)
    app.router.add_route('/about', about)
    app.router.add_route('/json', json_test)
    app.router.add_route('/text', text_test)
    app.run(debug=False, host='0.0.0.0', port=8000)
