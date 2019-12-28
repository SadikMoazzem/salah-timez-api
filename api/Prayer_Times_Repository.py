from datetime import datetime

from api import db
from api.models import PrayerTimes

class Prayer_Times_Repository:

    def get_today_salah_times():
        """
        Updating the status of a webpage

        :param webpage_id
        :return:
        """
        salah_start: PrayerTimes = db.session.query(PrayerTimes)\
            .filter((PrayerTimes.mosque_id == 0) & (PrayerTimes.date == datetime.now().strftime('%Y-%m-%d')))
        
        salah_jammats: PrayerTimes = db.session.query(PrayerTimes)\
            .filter((PrayerTimes.mosque_id == 1) & (PrayerTimes.date == datetime.now().strftime('%Y-%m-%d')))
        
        salah_response = {}
        
        for salah in salah_start:
            if not(salah.result()['salah'] in salah_response):
                salah_response[salah.result()['salah']] = salah.result()
            else:
                salah_response[salah.result()['salah']].update( salah.result())

        for salah in salah_jammats:
            if not(salah.result()['salah'] in salah_response):
                salah_response[salah.result()['salah']] = salah.result()
            else:
                salah_response[salah.result()['salah']].update( salah.result())

        return salah_response