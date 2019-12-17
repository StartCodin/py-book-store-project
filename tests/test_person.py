from src.person import Person

import pytest


@pytest.fixture
def person():
    return Person('Test Name', 'Test City')


def test_person_created_with_valid_arguments(person):
    assert person.name == 'Test Name' and person.city == 'Test City'


@pytest.mark.parametrize('name', [(n) for n in ('', 'A', 'AB', 'ABC', 'ABCD')])
def test_person_with_name_below_min_length_raises_value_error(person, name):
    with pytest.raises(ValueError):
        person.name = name


def test_person_with_name_over_max_length_raises_value_error(person):
    with pytest.raises(ValueError):
        person.name = 'ABCDEF' * 10


def test_person_with_city_below_min_length_raises_value_error(person):
    with pytest.raises(ValueError):
        person.city = ''


def test_person_with_city_over_max_length_raises_value_error(person):
    with pytest.raises(ValueError):
        person.city = 'ABCDE' * 5


def test_person_with_valid_name_sets_correctly(person):
    person.name = 'Vijay Shriram'
    assert person.name == 'Vijay Shriram'


def test_person_with_valid_city_sets_correctly(person):
    person.city = 'Mysuru'
    assert person.city == 'Mysuru'
