from pion import run, route


@route('/hello')
def hello():
    return 'hello world'


run()
