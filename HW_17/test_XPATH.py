
import pytest
from selenium.webdriver.common.by import By

full_name_input = 'Andrii Herashchenko'
email_input = 'mail@domain.com'
curr_addr_input = 'Ukraine, Kyiv, Bandery str'
perm_addr_input = 'Ukraine, Smila, Nezalezhnosti str'

'''Заповнити поля Full Name, Email, Current Address, Permanent Address позитивними (коректними) значеннями.
   Натиснути кнопку Submit'''

@pytest.mark.XPATH
def test_input_XPATH(demoqa_chrome):

    demoqa_chrome.find_element(By.XPATH, '//input[@id="userName"]').send_keys(full_name_input)
    demoqa_chrome.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys(email_input)
    demoqa_chrome.find_element(By.XPATH, '//textarea[@id="currentAddress"]').send_keys(curr_addr_input)
    demoqa_chrome.find_element(By.XPATH, '//textarea[@id="permanentAddress"]').send_keys(perm_addr_input)
    demoqa_chrome.find_element(By.XPATH, '//button[@id="submit"]').click()

    '''переконатись:
    у тому, що під формою з'явились дані;
    у тому, що дані відповідають введеним'''

    result_full_name = demoqa_chrome.find_element(By.XPATH, '//p[@id="name"]').text.split(':')[1]
    result_email = demoqa_chrome.find_element(By.XPATH, '//p[@id="email"]').text.split(':')[1]
    result_curr_addr = demoqa_chrome.find_element(By.XPATH, '//p[@id="currentAddress"]').text.split(':')[1]
    result_perm_addr = demoqa_chrome.find_element(By.XPATH, '//p[@id="permanentAddress"]').text.split(':')[1]

    compare_data = [result_full_name == full_name_input,
                    result_email == email_input,
                    result_curr_addr == curr_addr_input,
                    result_perm_addr == perm_addr_input]

    assert all(compare_data), ' дані не відповідають введеним'


'''Змінити значення поля Email на некоректне та переконатись що поле відреагувало відповідно (з'явився червоний контур)'''
@pytest.mark.XPATH
def test_mail_validation_XPATH(demoqa_chrome):
    demoqa_chrome.find_element(By.XPATH, '//input[@id="userEmail"]').send_keys('incorrectEmail')
    demoqa_chrome.find_element(By.XPATH, '//button[@id="submit"]').click()

    error_mailform = demoqa_chrome.find_element(By.XPATH, '//input[@type="email"][contains(@class, "error")]')

    assert error_mailform





