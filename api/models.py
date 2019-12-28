from api import db

class PrayerTimes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mosque_id = db.Column(db.Integer)
    salah = db.Column(db.String)
    type = db.Column(db.String)
    time = db.Column(db.DateTime)
    date = db.Column(db.DateTime)