from pion import run, route


@route('/hello')
def hello():
    return 'hello world'


run(host='127.0.0.1', port=8000)
