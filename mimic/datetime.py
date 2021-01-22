import random


class DateTime:
    @classmethod
    def date(cls, start=None, end=None, fmt=''):
        return None

    @classmethod
    def time(cls, start_hour=None, end_hour=None, fmt='24h'):
        return None

    @classmethod
    def datetime(cls, start_hour=None, end_hour=None, fmt='24h'):
        return None

    @classmethod
    def year(cls, start=1970, end=2020):
        return None

    @classmethod
    def month(cls, as_type=str):
        return None

    @classmethod
    def day(cls, as_type=str):
        return None

    @classmethod
    def hour(cls, fmt='24h'):
        return None

    @classmethod
    def minute(cls):
        return None

    @classmethod
    def second(cls):
        return None

    @classmethod
    def millisecond(cls):
        return None
