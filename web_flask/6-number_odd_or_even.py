#!/usr/bin/python3
"""Module app flask"""

from flask import Flask, render_template
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

@app.route('/number/<int:n>', strict_slashes=False)
def numInt(n):
    """route python"""
    return '%d is a number' % n

@app.route('/number_template/<int:n>', strict_slashes=False)
def numbertemplate(n):
    return render_template('5-number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numberoddeven(n):
    prop = 'odd'
    if n % 2 == 0:
        prop = 'even'
    return render_template('6-number_odd_or_even.html', n=n, prop="odd")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
