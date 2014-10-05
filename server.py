#!/usr/bin/env python

import os
from dhtest.app import App
from tornado.ioloop import IOLoop


def main():
    app = App()
    port = int(os.environ.get("PORT", 8080))
    app.listen(port)
    print "Listening on port {0}".format(port)
    IOLoop.instance().start()


if __name__ == "__main__":
    main()
