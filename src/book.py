from src.constants import *


class Book:
    def __init__(self, title, category, pages, edition, author, publisher, price):
        self.title = title
        self.category = category
        self.pages = pages
        self.edition = edition
        self.author = author
        self.publisher = publisher
        self.price = price
        self.registered_by = None
        self._interested_readers = []

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if new_category in CATEGORY:
            self._category = new_category
        else:
            raise ValueError('Category doesn\'t exist')

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages):
        if PAGES_MIN < new_pages < PAGES_MAX:
            self._pages = new_pages
        else:
            raise ValueError(
                f'Pages should be between {PAGES_MIN} and {PAGES_MAX}')

    @property
    def edition(self):
        return self._edition

    @edition.setter
    def edition(self, new_edition):
        if EDITION_MIN < new_edition < EDITION_MAX:
            self._edition = new_edition
        else:
            raise ValueError(
                f'Edition should be between {EDITION_MIN} and {EDITION_MAX}')

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if NAME_MIN_LENGTH < len(new_title) < NAME_MAX_LENGTH:
            self._title = new_title
        else:
            raise ValueError(
                f'Title name has to be between {NAME_MIN_LENGTH} and {NAME_MAX_LENGTH} chracters')

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if NAME_MIN_LENGTH < len(new_author) < NAME_MAX_LENGTH:
            self._author = new_author
        else:
            raise ValueError(
                f'Author name has to be between {NAME_MIN_LENGTH} and {NAME_MAX_LENGTH} chracters')

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, new_publisher):
        if NAME_MIN_LENGTH < len(new_publisher) < NAME_MAX_LENGTH:
            self._publisher = new_publisher
        else:
            raise ValueError(
                f'Publisher name has to be between {NAME_MIN_LENGTH} and {NAME_MAX_LENGTH} chracters')

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if PRICE_MIN < new_price < PRICE_MAX:
            self._price = new_price
        else:
            raise ValueError(
                f'Price should be between {PRICE_MIN} and {PRICE_MAX}')

    def register(self, staff):
        if self.registered_by == None:
            self.registered_by = staff
        else:
            raise Exception('Already registered')

    def _add_interested_reader(self, reader):
        if reader in self._interested_readers:
            raise Exception('User already added')
        else:
            self._interested_readers.append(reader)

    @property
    def interested_readers(self):
        return self._interested_readers
