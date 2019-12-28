import math
from flask import jsonify, request, render_template
from datetime import datetime, timedelta

from api import app, models
from api.Prayer_Times_Repository import Prayer_Times_Repository

@app.route('/')
def test():
    ret = """
        <HTML>
            <BODY>
                <H1>Endpoints</H1>
                <p>
                /salah - Will get you the current day salah times
                </p>
            </BODY>
        <HTML>
    """
    return ret

@app.route('/salah')
def index():
    calendar_id = request.args.get('calendar_id')
    if not calendar_id:
        calendar_id = 1

    salahs = Prayer_Times_Repository.get_today_salah_times()
  
    return jsonify({datetime.now().strftime('%Y-%m-%d'): salahs})