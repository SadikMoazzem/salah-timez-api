import math
import os
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
    print('/salah - Endpoint called')
    calendar_id = request.args.get('calendar_id')
    if not calendar_id:
        calendar_id = 1

    print('Starting work')
    res = {}
    date = datetime.now()

    res[date.strftime('%Y-%m-%d')] = Prayer_Times_Repository.get_salah_times(date)
    for i in range(6): 
        date += timedelta(days=1)
        res[date.strftime('%Y-%m-%d')] = Prayer_Times_Repository.get_salah_times(date)
    
    print('Work done')
    print('Response -' + str(res))
    return jsonify(res)

@app.before_request
def before_request_func():
    auth_request_token = request.headers.get('Authorization')
    print('token given : ' + str(auth_request_token))
    AUTH_TOKEN = 'Bearer ' + str(os.environ.get('AUTH_TOKEN'))
    # if AUTH_TOKEN != auth_request_token:
    #     response = jsonify({'NOT AUTHORIZED':'Token not valid!'})
    #     return response, 401