class ServerAdapter(object):
    def __init__(self, host='127.0.0.1', port=8000, **kargs):
        self.host = host
        self.port = int(port)
        self.options = kargs
    
    def __repr__(self):
        return "{} ({}:{})".format(self.__class__.__name__, self.host, self.port)

    def run(self, handler):
        pass


class WSGIRefServer(ServerAdapter):
    def run(self, handler):
        from wsgiref.simple_server import make_server
        server = make_server(self.host, self.port, handler)
        server.serve_forever()