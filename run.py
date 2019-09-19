from flask import Flask, jsonify, request, render_template
from data import salah_times
from datetime import datetime
import math

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

def intPart(floatNum):
    if floatNum < -0.0000001: return math.ceil(floatNum - 0.0000001)
    return math.floor(floatNum + 0.0000001)


def Gregorian2Hijri(yr, mth, day):
    jd1 = intPart((1461 * (yr + 4800 + intPart((mth - 14) / 12.0))) / 4)
    jd2 = intPart((367 * (mth - 2 - 12 * (intPart((mth - 14) /
                                                  12.0)))) / 12)
    jd3 = intPart((3 * (intPart((yr + 4900 + intPart((mth - 14) /
                                                     12.0)) / 100))) / 4)
    jd = jd1 + jd2 - jd3 + day - 32075

    l = jd - 1948440 + 10632
    n = intPart((l - 1) / 10631.0)
    l = l - 10631 * n + 354

    j1 = (intPart((10985 - l) / 5316.0)) * (intPart((50 * l) / 17719.0))
    j2 = (intPart(l / 5670.0)) * (intPart((43 * l) / 15238.0))
    j = j1 + j2

    l1 = (intPart((30 - j) / 15.0)) * (intPart((17719 * j) / 50.0))
    l2 = (intPart(j / 16.0)) * (intPart((15238 * j) / 43.0))
    l = l - l1 - l2 + 29

    m = intPart((24 * l) / 709.0)
    y = 30 * n + j - 30
    d = l - intPart((709 * m) / 24.0)
    return y, m, d


@app.route('/')
def test():
    ret = """
        <HTML>
            <BODY>
                <H1>Endpoints</H1>
                <BR/>
                <H3>
                /Salah - Will get you the current day salah times
                </H3>
            </BODY>
        <HTML>
    """
    return ret


@app.route('/salah')
def index():
    today = datetime.today()
    months = ["JAN" ,"FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEPT", "OCT", "NOV", "DEC"]
    current_month = months[today.month-1]
    currentDay = today.day
    salah_times_month = salah_times[current_month]

    salah_times_today = {
        "fajir_start": salah_times_month["fajir_start"]["{}".format(currentDay)],
        "fajir_jammat": salah_times_month["fajir_jammat"]["{}".format(currentDay)],
        "sunrise": salah_times_month["sunrise"]["{}".format(currentDay)],
        "zuhr_start": salah_times_month["zuhr_start"]["{}".format(currentDay)],
        "zuhr_jammat": salah_times_month["zuhr_jammat"]["{}".format(currentDay)],
        "asr_1_start": salah_times_month["asr_1_start"]["{}".format(currentDay)],
        "asr_2_start": salah_times_month["asr_2_start"]["{}".format(currentDay)],
        "asr_jammat": salah_times_month["asr_jammat"]["{}".format(currentDay)],
        "magrib_start": salah_times_month["magrib_start"]["{}".format(currentDay)],
        "magrib_jammat": salah_times_month["magrib_jammat"]["{}".format(currentDay)],
        "isha_start": salah_times_month["isha_start"]["{}".format(currentDay)],
        "isha_jammat": salah_times_month["isha_jammat"]["{}".format(currentDay)],
    }
    return jsonify(salah_times_today)


if __name__ == '__main__':
    app.run()
