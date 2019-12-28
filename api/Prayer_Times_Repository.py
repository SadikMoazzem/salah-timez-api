from api import db

from api.models import PrayerTimes

class Prayer_Times_Repository:

    def get_today_salah_times():
        """
        Updating the status of a webpage

        :param webpage_id
        :return:
        """
        webpages: Webpage = db.session.query(PrayerTimes)\
            .filter(PrayerTimes.id == 11)
        
        return webpages
