#!/usr/bin/python3
""" starts a Flask web application"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display hbnb"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_is_fun(text):
    """displaty c is fun"""
    return "C %s" % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_is_cool(text="is cool"):
    """display Python is ..."""
    return "Python %s" % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
