
import pytest


uniq = ['Radament', 'Dark Elder', 'Ismail', 'Geleb', 'Fangskin', 'Andy', 'Duriq'] #list for tests 1 and 3
@pytest.mark.param
@pytest.mark.parametrize('council_member', ['Ismail', 'Geleb'])
def test_one(council_member):
    assert council_member in uniq
    print(f'\n{council_member} is the Council member')

@pytest.mark.param
@pytest.mark.parametrize('input, expected', [('4', 4), ('42', 42), ('-1', -1)])
def test_two(input, expected):
    assert int(input) == expected

@pytest.mark.param
@pytest.mark.parametrize('name', ['Andy', 'Duriq'], ids=['1act', '2act'])

def test_three(name):
    assert name in uniq
