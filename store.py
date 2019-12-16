from constants import *
from receipt import Receipt
from datetime import date
import json


class Store:
    def __init__(self, name):
        self.name = name
        self._books = []
        self._receipts = []

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

    def add_book(self, book):
        if book in self._books:
            raise Exception('Book already added')
        else:
            self._books.append(book)

    @property
    def books(self):
        return self._books

    def buy_book(self, book, reader, staff):
        receipt = Receipt(book, reader, date.today(), staff)
        self._receipts.append(receipt)
        return receipt.id

    def add_interested_reader(self, book, reader):
        book._add_interested_reader(reader)

    def print_receipt(self, receipt_id):
        receipts = [r for r in self._receipts if (r.id == receipt_id)]
        if len(receipts) > 0:
            receipt = receipts[0]
            print(receipt.details)
        else:
            Exception('Cannot find the receipt')
