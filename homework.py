import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys


sbis_site = "https://test.saby.ru/"
sbis_title = "Saby — экосистема для управления бизнесом"
driver = webdriver.Chrome()

try:
	driver.get(sbis_site)
	assert driver.current_url == sbis_site, "Не верный сайт"
	time.sleep(5)
	assert driver.title == sbis_title, "Не верный заголовок"
	tabs = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item')

	start_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Button--primary')
	assert start_btn.text == "Начать работу"
	assert start_btn.get_attribute('title') == "Начать работу"
	assert start_btn.is_displayed()
	start_btn.click()
	time.sleep(5)
	driver.switch_to.window(driver.window_handles[1])
	login = driver.find_element(By.CSS_SELECTOR, '[name="ws-input_2025-02-23"]')
	login.send_keys('testadminmaks', Keys.ENTER)
	assert login.get_attribute('value') == 'testadminmaks'





finally:
	driver.quit()