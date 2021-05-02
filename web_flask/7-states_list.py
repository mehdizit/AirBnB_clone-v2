#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list')
def display_states_list():
    """disolay states"""
    return render_template('7-states_list.html', storage=storage.all('State'))


@app.teardown_appcontext
def close(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
