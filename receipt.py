from constants import *
import jsonpickle
from datetime import date, time


class Receipt:
    _counter = 1

    def __init__(self, book, reader, date, staff):
        self._id = Receipt._counter
        self.book = book
        self.reader = reader
        self.date = date
        self.staff = staff
        self.amount = book.price

        Receipt._counter += 1

    @staticmethod
    def serialize(obj):

        if isinstance(obj, date):
            serial = obj.isoformat()
            return serial

        if isinstance(obj, time):
            serial = obj.isoformat()
            return serial

        return obj.__dict__

    @property
    def details(self):
        return jsonpickle.encode(self, unpicklable=False)

    @property
    def id(self):
        return self._id
