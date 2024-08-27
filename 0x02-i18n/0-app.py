#!/usr/bin/env python3
"""
Flask app that outputs “Welcome to Holberton” & “Hello world”
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
