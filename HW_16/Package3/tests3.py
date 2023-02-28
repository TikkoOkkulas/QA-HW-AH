
'''В третьому пакунку створити довільну кількість тестів (але не менше 3-х), організованих довільно,
але на конжному має бути 2 мітки: одна спільна для усіх тестів в цьому пакунку ("pack"),
інша -- спільна для як мінімум 2-х тестів ("joint"), і ще інша для остачі тестів ("rest").
На кожен тест в пакунку має бути застосована фікстура.'''

import pytest

@pytest.mark.pack
@pytest.mark.joint
def test_one(func_fixture):
    print(f'\nrun test 1')
    pass

@pytest.mark.pack
@pytest.mark.rest
def test_two(func_fixture):
    print('\nrun test 2')
    pass

@pytest.mark.pack
@pytest.mark.joint
def test_three(func_fixture):
    print('\nrun test 3')
    pass

@pytest.mark.pack
@pytest.mark.rest
def test_four(func_fixture):
    print('\nrun test 4')
    pass

@pytest.mark.pack
@pytest.mark.rest
def test_five(func_fixture):
    print('\nrun test 5')
    pass
