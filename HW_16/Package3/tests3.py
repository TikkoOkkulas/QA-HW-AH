

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