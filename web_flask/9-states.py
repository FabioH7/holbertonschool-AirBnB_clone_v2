#!/usr/bin/python3
"""First flask app"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage


app = Flask(__name__)
""" Flask app module"""


@app.route("/states", strict_slashes=False)
def state_list():
    """ Route that prints hello """
    states = storage.all("State").values()
    return render_template('9-states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def state_city_list(id):
    """ Route that prints hello """
    state = None
    states = storage.all("State").values()
    for element in states:
        if element.id == id:
            state = element
    return render_template('9-states.html',
                           state=state)


@ app.teardown_appcontext
def close_storage(self):
    storage.close()


if __name__ == '__main__':
    """ sa per siguri """
    app.run(host='0.0.0.0', port=5000)
