#!/usr/bin/python3
"""Module app flask"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def route_cities():
    """start web app"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """close storage"""
    storage.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
