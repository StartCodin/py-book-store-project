from src.reader import Reader

import pytest


@pytest.fixture
def reader():
    return Reader('Test Name', 'Test City', 'reader@domain.com', '1234567890')


@pytest.mark.parametrize('reader, email', [(reader, email) for email in ['person@domain.com', 'per@dom.co.in']])
def test_reader_accepts_valid_emails(reader, email):
    reader.email = email
    assert reader.email == email
