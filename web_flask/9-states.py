#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """disolay states"""
    return render_template('7-states_list.html', storage=storage.all('State'))


@app.route('/states/<id>', strict_slashes=False)
def display_by_id(id):
    state_obj = None
    for obj in storage.all("State").values():
        if obj.id == id:
            state_obj = obj

    return render_template('9-states.html', storage=storage.all('State'),
                           state_obj=state_obj)


@app.teardown_appcontext
def close(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
