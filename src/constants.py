NAME_MIN_LENGTH = 5
NAME_MAX_LENGTH = 50

CITY_MIN_LENGTH = 3
CITY_MAX_LENGTH = 20

# https://emailregex.com/
EMAIL_REGEX = '''(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''

PHONE_MIN_LENGTH = 10
PHONE_MAX_LENGTH = 11
PHONE_REGEX = '''^[0-9]*$'''

CATEGORY = {'Novel', 'Current Affairs', 'Biography', 'Comics',
            'Children', 'Textbook', 'Reference', 'Dictionary'}

PAGES_MIN = 25
PAGES_MAX = 1500

EDITION_MIN = 1
EDITION_MAX = 1000


PRICE_MIN = 0
PRICE_MAX = 10000
