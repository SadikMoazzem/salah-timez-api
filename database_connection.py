import sqlalchemy as db
from sqlalchemy import String

engine = db.create_engine('postgres://xmvnosuwbdebpw:65a76a6a5427a150a8a9465573fb01734429eaccc7cdbb8eee2123d09d5f73a7@ec2-54-247-72-30.eu-west-1.compute.amazonaws.com:5432/d2kptkfgq2lunm')

def get_today_salah_times(calendar_id, month, day):
    # Setup
    connection = engine.connect()
    metadata = db.MetaData()
    salah_times = db.Table('salah_times', metadata,
        db.Column('day',String),
        db.Column('month',String),
        db.Column('salah',String),
        db.Column('time',String),
        autoload=True, autoload_with=engine)

    # # Select data via select() construct
    select_st = db.select([
            salah_times.columns.day,
            salah_times.columns.month,
            salah_times.columns.salah,
            salah_times.columns.time
        ]).where(
        (salah_times.columns.calendar_id == calendar_id) &
        (salah_times.columns.month == month) &
        (salah_times.columns.day == day)
    )
    res = engine.execute(select_st)
    result = {}
    for i in res:
        result[i[2]] = i[3]
    connection.close()

    return {day: result}
