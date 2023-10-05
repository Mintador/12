
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)

def testing():
   pytest.driver = webdriver.Firefox('C:\geckodriver-v0.33.0-win')
   # Переходим на страницу авторизации
   pytest.driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth/?client_id=lk_onlime&redirect_uri=https%3A%2F%2Fmy.rt.ru%2Fauth%2Fssoredirect%2F&response_type=code&auth_type=standard')

   yield

   pytest.driver.quit()


def test_mail_success():
   # Вводим email
   pytest.driver.find_element(By.ID, 'username').send_keys('egoritch4321@yandex.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('Zabrodin128547')
   sleep(5)
   form.btn_click()

   assert form.get_current_url() == ('https://b2c.passport.rt.ru/account_b2c/page?state=e728aaee-6404-4c16-b788-2558fd71fabc&client_id=account_b2c#/')

   pytest.driver.close()

def test_mail_failure():
   # Вводим email
   pytest.driver.find_element(By.ID, 'username').send_keys('egoritch4321@yandex.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('128547')
   sleep(5)
   form.btn_click()
   sleep(5)
   # Проверка сообщения об ошибке
   error_message = driver.find_element(By.CLASS_NAME,'error-message')
   assert 'Неверный логин или пароль' in error_message.text
   pytest.driver.close()

def test_pass_failure():
   # Вводим email
   pytest.driver.find_element(By.ID, 'username').send_keys('124235')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('Zabrodin128547')
   sleep(5)
   form.btn_click()
   sleep(5)
   # Проверка сообщения об ошибке
   error_message = driver.find_element(By.CLASS_NAME,'error-message')
   assert 'Неверный логин или пароль' in error_message.text
   pytest.driver.close()

def test_number_success():
   phone_tab = find_element(By.ID, 't-btn-tab-phone')
   phone_tab.click()
   sleep(5)
   # Вводим номер
   pytest.driver.find_element(By.ID, 'username').send_keys('89252277336')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('Zabrodin128547')
   sleep(5)
   form.btn_click()
   sleep(5)

   assert form.get_current_url() == ('https://b2c.passport.rt.ru/account_b2c/page?state=e728aaee-6404-4c16-b788-2558fd71fabc&client_id=account_b2c#/')

   pytest.driver.close()

def test_number_failure():
   phone_tab = find_element(By.ID, 't-btn-tab-phone')
   phone_tab.click()
   sleep(5)
   # Вводим номер
   pytest.driver.find_element(By.ID, 'username').send_keys('892543533547336')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('Zabrodin128547')
   sleep(5)
   form.btn_click()
   sleep(5)
   # Проверка сообщения об ошибке
   error_message = driver.find_element(By.CLASS_NAME,'error-message')
   assert 'Неверный логин или пароль' in error_message.text
   pytest.driver.close(

def test_login_success():
   phone_tab = find_element(By.ID, 't-btn-tab-login')
   phone_tab.click()
   sleep(5)
   # Вводим номер
   pytest.driver.find_element(By.ID, 'username').send_keys('egoritch4321@yandex.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('Zabrodin128547')
   sleep(5)
   form.btn_click()
   sleep(5)

   assert form.get_current_url() == ('https://b2c.passport.rt.ru/account_b2c/page?state=e728aaee-6404-4c16-b788-2558fd71fabc&client_id=account_b2c#/')

   pytest.driver.close()

def test_login_failure():
   phone_tab = find_element(By.ID, 't-btn-tab-login')
   phone_tab.click()
   sleep(5)
   # Вводим номер
   pytest.driver.find_element(By.ID, 'username').send_keys('egoritch4321@yandex.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('Zabrodin128547')
   sleep(5)
   form.btn_click()
   sleep(5)
   # Проверка сообщения об ошибке
   error_message = driver.find_element(By.CLASS_NAME,'error-message')
   assert 'Неверный логин или пароль' in error_message.text
   pytest.driver.close()

def test_ls_success():
   phone_tab = find_element(By.ID, 't-btn-tab-ls')
   phone_tab.click()
   sleep(5)
   # Вводим номер
   pytest.driver.find_element(By.ID, 'username').send_keys('14224256451322 ')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('Zabrodin128547')
   sleep(5)
   form.btn_click()
   sleep(5)

   assert form.get_current_url() == ('https://b2c.passport.rt.ru/account_b2c/page?state=e728aaee-6404-4c16-b788-2558fd71fabc&client_id=account_b2c#/')

   pytest.driver.close()

def test_ls_failure():
   phone_tab = find_element(By.ID, 't-btn-tab-ls')
   phone_tab.click()
   sleep(5)
   # Вводим номер
   pytest.driver.find_element(By.ID, 'username').send_keys('14224256451322 ')
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'password').send_keys('Zabrodin128547')
   sleep(5)
   form.btn_click()
   sleep(5)
   # Проверка сообщения об ошибке
   error_message = driver.find_element(By.CLASS_NAME,'error-message')
   assert 'Неверный логин или пароль' in error_message.text
   pytest.driver.close()