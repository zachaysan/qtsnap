import tornado.ioloop
import tornado.web
from tornado import template
from qt.analyzers.user import UserComments

loader = template.Loader("qt/views")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(loader.load("index.html").generate())

class UserHandler(tornado.web.RequestHandler):
    def get(self, username):
        self.write(username)

application = tornado.web.Application([
    (r"/", MainHandler),
])

def run():
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
