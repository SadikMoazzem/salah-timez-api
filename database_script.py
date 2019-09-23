from data import salah_times
import sqlalchemy as db
from datetime import date

engine = db.create_engine('postgres://xmvnosuwbdebpw:65a76a6a5427a150a8a9465573fb01734429eaccc7cdbb8eee2123d09d5f73a7@ec2-54-247-72-30.eu-west-1.compute.amazonaws.com:5432/d2kptkfgq2lunm')

month_dict = {
    'JAN' : '1',
    'FEB' : '2',
    'MAR' : '3',
    'APR' : '4',
    'MAY' : '5',
    'JUN' : '6',
    'JUL' : '7',
    'AUG' : '8',
    'SEPT' : '9',
    'OCT' : '10',
    'NOV' : '11',
    'DEC' : '12',
}

# Setup
connection = engine.connect()
metadata = db.MetaData()
# salah_times_db = db.Table('salah_times', metadata, autoload=True, autoload_with=engine)

salahs = []

for month in salah_times:
    for salah in salah_times[month]:
        for day in salah_times[month][salah]:
            salah_times_db = db.Table('salah_times', metadata, autoload=True, autoload_with=engine)
            print('MONTH ' + month_dict[month] + ' | DAY ' + day + ' | SALAH ' + salah + ' | SALAH TIME ' + salah_times[month][salah][day])
            # insert data via insert() construct
            insert_salah = salah_times_db.insert().values(
                month=month_dict[month],
                day=day,
                salah=salah,
                time=salah_times[month][salah][day],
                calender_id='1'
            )

            engine.execute(insert_salah)
            # salahs.append({
            #     'month': month_dict[month],
            #     'day': day,
            #     'salah': salah,
            #     'time' : salah_times[month][salah][day]
            # })

connection.close()

# print(salahs)