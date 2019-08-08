from calendar import timegm
from datetime import datetime


def epoch_seconds(dt: datetime = datetime.now()):
    parts = datetime.timetuple(dt)
    es = timegm(parts)
    return es
