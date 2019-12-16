from src.person import *
import re


class Reader(Person):

    def __init__(self, name, city, email, phone):
        super().__init__(name, city)
        self.email = email
        self.phone = phone

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if re.match(EMAIL_REGEX, new_email):
            self._email = new_email
        else:
            raise ValueError('Email is not proper')

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, new_phone):
        if (PHONE_MIN_LENGTH < len(new_phone)) or (len(new_phone) > PHONE_MAX_LENGTH):
            raise ValueError(
                f'Phone number has to be either {PHONE_MIN_LENGTH} or {PHONE_MAX_LENGTH}')
        elif not re.match(PHONE_REGEX, new_phone):
            raise ValueError(f'Phone number is improper')
        else:
            self._phone = new_phone
