'''В першому пакунку створтити файл з 5 тестами, що знаходяться у класі. Перед та після тестів повинна відпрацювати
фікстура, що виведе в консоль повідомлення про початок та кінець свого виконання. Нехай тести також виведуть в консоль
що небудь. На усі тести поставити мітку "from_class".'''

import pytest

@pytest.fixture(scope='class', autouse=True)
def class_fixture():
    print('\nText from fixture before all tests')
    yield
    print('\nText from fixture after all tests')