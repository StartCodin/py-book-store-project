import pytest

import logging

logger = logging.getLogger()


@pytest.hookimpl()
def pytest_sessionstart(session):
    logger.info(f'Starting pytest session')


@pytest.hookimpl()
def pytest_sessionfinish(session, exitstatus):
    logger.info(f'Ending pytest session with exit status: {exitstatus}')


@pytest.hookimpl()
def pytest_runtest_call(item):
    logger.info(f'Executing test: {item}')
