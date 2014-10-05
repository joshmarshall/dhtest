from tornado.web import Application
from dhtest.index_handler import IndexHandler


class App(Application):

    def __init__(self):
        routes = [("/(\d+)/(\d+)", IndexHandler)]
        return super(App, self).__init__(routes)
