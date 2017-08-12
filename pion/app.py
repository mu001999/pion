from server import WSGIRefServer


def run(server=WSGIRefServer, host='127.0.0.1', port=8000, optinmize=False, **kargs):
    server = server(host=host, port=port, **kargs)
    server.run(WSGIHandler)