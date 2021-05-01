#!/usr/bin/python3
"""Module app flask"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """start web app"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """route hbnb"""
    return 'HBNB'

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonFun(text='is cool'):
    """route python"""
    s = text.replace('_', ' ')
    return 'Python {}'.format(s)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
