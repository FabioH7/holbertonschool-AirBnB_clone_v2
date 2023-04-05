#!/usr/bin/python3
"""First flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


app = Flask(__name__)
""" Flask app module"""


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ Route that prints hello """
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()

    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@ app.teardown_appcontext
def close_storage(self):
    storage.close()


if __name__ == '__main__':
    """ sa per siguri """
    app.run(host='0.0.0.0', port=5000)
