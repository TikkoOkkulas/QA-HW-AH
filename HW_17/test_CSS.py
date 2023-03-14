
import pytest
from selenium.webdriver.common.by import By

full_name_input = 'Andrii Herashchenko'
email_input = 'mail@domain.com'
curr_addr_input = 'Ukraine, Kyiv, Bandery str'
perm_addr_input = 'Ukraine, Smila, Nezalezhnosti str'

'''Заповнити поля Full Name, Email, Current Address, Permanent Address позитивними (коректними) значеннями.
    Натиснути кнопку Submit'''
@pytest.mark.CSS
def test_input_CSS(demoqa_chrome):
    demoqa_chrome.find_element(By.CSS_SELECTOR, '#userName').send_keys(full_name_input)
    demoqa_chrome.find_element(By.CSS_SELECTOR, '#userEmail').send_keys(email_input)
    demoqa_chrome.find_element(By.CSS_SELECTOR, '#currentAddress').send_keys(curr_addr_input)
    demoqa_chrome.find_element(By.CSS_SELECTOR, '#permanentAddress').send_keys(perm_addr_input)
    demoqa_chrome.find_element(By.CSS_SELECTOR, '#submit').click()

    '''переконатись:
    у тому, що під формою з'явились дані;
    у тому, що дані відповідають введеним'''

    result_full_name = demoqa_chrome.find_element(By.CSS_SELECTOR, '#name').text.split(':')[1]
    result_email = demoqa_chrome.find_element(By.CSS_SELECTOR, '#email').text.split(':')[1]
    result_curr_addr = demoqa_chrome.find_element(By.CSS_SELECTOR, 'p#currentAddress').text.split(':')[1]
    result_perm_addr = demoqa_chrome.find_element(By.CSS_SELECTOR, 'p#permanentAddress').text.split(':')[1]

    compare_data = [result_full_name == full_name_input,
                    result_email == email_input,
                    result_curr_addr == curr_addr_input,
                    result_perm_addr == perm_addr_input]

    assert all(compare_data), ' дані не відповідають введеним'


'''Змінити значення поля Email на некоректне та переконатись що поле відреагувало відповідно (з'явився червоний контур)'''
@pytest.mark.CSS
def test_mail_validation_CSS(demoqa_chrome):
    demoqa_chrome.find_element(By.CSS_SELECTOR, '#userEmail').send_keys('incorrectEmail.com')
    demoqa_chrome.find_element(By.CSS_SELECTOR, '#submit').click()

    error_mailform = demoqa_chrome.find_element(By.CSS_SELECTOR, '#userEmail[class~=field-error]')

    assert error_mailform