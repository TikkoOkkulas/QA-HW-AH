
import pytest

@pytest.fixture(scope='function', autouse=True)
def func_fixture():
    print('\nText from fixture before each test')
    yield
    print('\nText from fixture after each test')