from src.book import Book
from src.staff import Staff

import pytest


@pytest.fixture
def book():
    return Book('Test Book', 'Textbook', 900, 2, 'Test Author', 'Test Publisher', 1000)


@pytest.fixture
def staff():
    return Staff('Test Staff', 'Test City')


def test_register(book, staff):
    book.register(staff)
    assert book.registered_by == staff
