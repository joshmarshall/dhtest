from PIL import Image
from random import randint
from multiprocessing import Process, Queue
import sys

from tornado.concurrent import Future
from tornado.ioloop import IOLoop


class Imager(object):

    def __init__(self, width, height):
        self._future = Future()
        self._ioloop = IOLoop.instance()
        self._ioloop.add_callback(self._timeout)
        self._queue = Queue()
        self._process = Process(
            target=_start, args=[width, height, self._queue])

    def start(self):
        self._process.start()
        return self._future

    def _timeout(self):
        if self._queue.empty():
            self._ioloop.add_callback(self._timeout)
            return
        image = self._queue.get()
        self._future.set_result(image)


def _start(width, height, queue):
    # should use numpy for this...
    pixels = []
    for pixel in range(width * height):
        pixels.append((randint(0, 255), randint(0, 255), randint(0, 255)))
    image = Image.new("RGB", (width, height))
    image.putdata(pixels)
    queue.put(image)


def main():
    width, height = sys.argv[1:3]
    imager = Imager(int(width), int(height))
    ioloop = IOLoop.instance()

    def _done(f):
        image = f.result()
        print image
        image.save(sys.stdout, format="JPEG", quality=85)
        ioloop.stop()

    ioloop.add_future(imager.start(), _done)
    ioloop.start()


if __name__ == "__main__":
    main()
