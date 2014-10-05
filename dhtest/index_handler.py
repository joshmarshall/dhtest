from StringIO import StringIO
from tornado import gen
from tornado.web import RequestHandler

from dhtest.awesome import Imager


class IndexHandler(RequestHandler):

    @gen.coroutine
    def get(self, width, height):
        imager = Imager(int(width), int(height))
        image = yield imager.start()
        self.set_header("Content-type", "image/jpeg")
        output = StringIO()
        image.save(output, format="JPEG", quality=85)
        output.seek(0)
        self.finish(output.read())
