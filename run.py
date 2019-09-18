from flask import Flask, jsonify, request, render_template
from data import SalahData

from datetime import date
import logging

app = Flask(__name__)

# Product API
@app.route('/')
def test():
    return "OK!"

# Product API
@app.route('/status')
def hello():
    return SalahData


if __name__ == '__main__':
    app.run()
