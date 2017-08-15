# Pion
Pion is simple and easy to learn.

### Example
```python
# hello.py

from pion import run, route


@route('/hello')
def hello():
    return 'Hello World'


run(host='127.0.0.1', port=8000)
```

### TODO
Make it async.
