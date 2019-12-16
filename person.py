from constants import *


class Person:
    _counter = 1

    def __init__(self, name, city):
        self.name = name
        self._id = Person._counter
        self.city = city

        Person._counter += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if NAME_MIN_LENGTH < len(new_name) < NAME_MAX_LENGTH:
            self._name = new_name
        else:
            raise ValueError(
                f'Name has to be between {NAME_MIN_LENGTH} and {NAME_MAX_LENGTH} chracters')

    @property
    def id(self):
        return self._id

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, new_name):
        if CITY_MIN_LENGTH < len(new_name) < CITY_MAX_LENGTH:
            self._city = new_name
        else:
            raise ValueError(
                f'City has to be between {CITY_MIN_LENGTH} and {CITY_MAX_LENGTH} chracters')
