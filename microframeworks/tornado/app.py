import tornado.ioloop
import tornado.web
import ujson
from microframeworks.settings import HOST, PORT, JSON_DATA, TEXT

class TextHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(TEXT)

class JsonHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(ujson.dumps(JSON_DATA))

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Tornado')


def make_app():
    return tornado.web.Application([
        (r"/text", TextHandler),
        (r"/json", JsonHandler),
        (r"/about", AboutHandler),
    ], debug=False)

if __name__ == "__main__":
    print("Tornado server running")
    app = make_app()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()