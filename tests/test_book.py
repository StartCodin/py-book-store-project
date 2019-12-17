from src.book import Book
from src.staff import Staff

import pytest
from unittest.mock import Mock


@pytest.fixture
def book():
    return Book('Test Book', 'Textbook', 900, 2, 'Test Author', 'Test Publisher', 1000)


@pytest.fixture
def staff():
    staff_stub = Mock(Staff)
    staff_stub.name.return_value = 'Stub Staff'
    return staff_stub


def test_register(book, staff):
    book.register(staff)
    assert book.registered_by == staff


def test_registration_has_the_staff_name(book, staff):
    book.register(staff)
    assert book.registered_by.name == staff.name
