from src.book import Book
from src.staff import Staff
from src.constants import *

import pytest
from unittest.mock import Mock


@pytest.fixture
def book():
    return Book('Test Book', 'Textbook', 900, 2, 'Test Author', 'Test Publisher', 1000)


@pytest.mark.parametrize('book, category', [(book, cat) for cat in CATEGORY])
def test_category_in_the_list_is_accepted(book, category):
    book.category = category
    assert book.category == category
