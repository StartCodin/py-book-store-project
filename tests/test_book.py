from src.book import Book
from src.staff import Staff
from src.constants import *

import pytest
from unittest.mock import Mock

import logging

logger = logging.getLogger()

# procedure:
# import logging and set logger
# inside the tests, write log messages
# at the project level create the pytest.ini file
# set log_cli and other properties
# more information: https://docs.pytest.org/en/latest/logging.html#live-logs


@pytest.fixture
def book():
    return Book('Test Book', 'Textbook', 900, 2, 'Test Author', 'Test Publisher', 1000)


@pytest.mark.parametrize('book, category', [(book, cat) for cat in CATEGORY])
def test_category_in_the_list_is_accepted(book, category):
    book.category = category
    logger.info(f'category set to: {category}')
    assert book.category == category
