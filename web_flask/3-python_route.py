#!/usr/bin/python3
"""First flask app"""
from flask import Flask

app = Flask(__name__)
""" Flask app module"""


@app.route("/", strict_slashes=False)
def first_route():
    """ Route that prints hello """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def second_route():
    """ Route that prints hello """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def third_route(text):
    """ Route that prints hello """
    return "C {}".format(text.replace('_', " "))


@app.route("/python", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def fourth_route(text='is_cool'):
    """ Route that prints hello """
    return "Python {}".format(text.replace('_', " "))


if __name__ == '__main__':
    """ sa per siguri """
    app.run(host='0.0.0.0', port=5000, debug=True)
