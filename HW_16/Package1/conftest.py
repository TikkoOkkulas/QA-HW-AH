
import pytest

@pytest.fixture(scope='class', autouse=True)
def class_fixture():
    print('\nText from fixture before all tests')
    yield
    print('\nText from fixture after all tests')