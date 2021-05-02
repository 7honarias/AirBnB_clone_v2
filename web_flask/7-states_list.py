#!/usr/bin/python3
"""Module app flask"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)

dict_state = None
@app.route('/', strict_slashes=False)
def index():
    """start web app"""
    return "Hello!!!"


@app.route('/states_list', strict_slashes=False)
def hello_route():
    """start web app"""
    dict_state = storage.all(State)
    return render_template('7-states_list.html', dict_state=dict_state)


@app.teardown_appcontext
def teardown_db(exception):
    """close storage"""
    if dict_state != None:
        storage.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
