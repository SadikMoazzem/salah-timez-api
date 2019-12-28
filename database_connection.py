from run import db
from flask_sqlalchemy import String

from PrayerTimes import PrayerTimes

engine = db.create_engine('postgres://jggkphnqehagqp:6a13df78dd9ce1e1b8ed9a76cd42e37f9b55587a3372b8ffda814f3294810d93@ec2-176-34-184-174.eu-west-1.compute.amazonaws.com:5432/dco45j4dohrfho')

def get_today_salah_times():
    # Setup
    connection = engine.connect()
    metadata = db.MetaData()

    # # Select data via select() construct
    select_st = db.select(PrayerTimes)
    
    res = engine.execute(select_st)
    # result = {}
    for i in res:
        print(i)
    # connection.close()

    # return {day: result}

get_today_salah_times()