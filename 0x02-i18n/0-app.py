#!/usr/bin/env python3
"""
Flask app that outputs “Welcome to Holberton” & “Hello world”
"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index() -> str:
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
