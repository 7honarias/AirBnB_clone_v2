#!/usr/bin/python3
"""Module app flask"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def hello_route():
    """start web app"""
    all_state = {}
    dict_state = storage.all(State)
    for key, state in dict_state.items():
        all_state[state.name] = state
    return render_template('7-states_list.html', dict_state=all_state)


@app.teardown_appcontext
def teardown_db(exception):
    """close storage"""
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
