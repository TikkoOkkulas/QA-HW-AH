
'''Використовуючи фікстуру, перейти на сторінку https://demoqa.com/text-box'''

import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def demoqa_chrome():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/text-box')
    yield driver
    driver.quit()
