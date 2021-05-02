#!/usr/bin/python3
"""Module app flask"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states/<id>', strict_slashes=False)
@app.route('/states', strict_slashes=False)
def route_states(id=None):
    """start web app"""
    all_state = {}
    dict_state = storage.all(State)
    
    if id is None:
        for key, state in dict_state.items():
            all_state[state.name] = state
    else:
        for key, state in dict_state.items():
            if state.id == id:
                all_state[state.name] = state
    print(len(all_state))
    return render_template('9-states.html', dict_state=all_state)


@app.teardown_appcontext
def teardown_db(exception):
    """close storage"""
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
