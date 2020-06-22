#!/usr/bin/env python3
from pycnic.core import WSGI, Handler

class QuoteRes():
    def get(self):
        return { 
            "quote":"Cool URIs don't change",
            "author":"Tim Berners-Lee"
        }

class app(WSGI):
    routes = [('/', QuoteRes())]

if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    print("Serving on 0.0.0.0:8080...")
    make_server('0.0.0.0', 8080, app).serve_forever()

#pip install gunicorn
#pip install uwsgi
#pip install wsgiref
