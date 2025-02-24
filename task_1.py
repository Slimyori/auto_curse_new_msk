# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys



sbis_site = "https://test.saby.ru/"
sbis_title = "Saby — экосистема для управления бизнесом"

sbis_contacts_site = 'https://test.saby.ru/contacts/66-sverdlovskaya-oblast?tab=clients'
sbis_contacts_title = 'Saby Контакты — Свердловская область'

tensor_site = 'https://tensor.ru/'
tensor_title = "Тензор — IT-компания"

tensor_site_about = 'https://tensor.ru/about'
tensor_site_about_title = 'О компании | Тензор — IT-компания'

driver = webdriver.Chrome()

#Переменные для сравнения
contacts_chek = "Контакты"
tensor_chek = 'Сила в людях'
tensor_button_text = 'Подробнее'

try:
	driver.get(sbis_site) #Открываем Сбис.ру (Сейчас саби.ру)
	assert driver.current_url == sbis_site, "Не верный сайт"
	time.sleep(5)
	assert driver.title == sbis_title, "Не верный заголовок"

	#Работа с вкладкой Контакты, в текстовом файле 11 вебинара предлагают через хреф искать, тогда в подвале есть сразу вкладка и переход на страницу, в моем случае кликаем в выпадающий список
	contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-link.sbis_ru-Header__menu-link.sbisru-Header__menu-link--hover')
	assert contacts.text == contacts_chek
	contacts.click()
	time.sleep(5)

	contacts_next = driver.find_element(By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu__arrow-icon")
	contacts_next.click()

	#Работа с сайтом контактов на саби.ру
	time.sleep(5)
	assert driver.title == sbis_contacts_title, "Не верный заголовок"
	assert driver.current_url == sbis_contacts_site, "Не верный сайт"
	time.sleep(5)
	tensor_next = driver.find_element(By.CSS_SELECTOR, '[alt="Разработчик системы Saby — компания «Тензор»"]')
	tensor_next.click()
	time.sleep(5)

	#Работа с тензор ру
	handles = driver.window_handles
	driver.switch_to.window(handles[1])
	time.sleep(2)
	assert driver.title == tensor_title, "Не верный заголовок"
	assert driver.current_url == tensor_site, "Не верный сайт"
	time.sleep(5)
	news_text = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content.tensor_ru-Index__card") #Блок новости
	assert tensor_chek in news_text.text, 'Не нашли новость Сила в людях' # Проверяем входил ли Сила в людях в блок новости

	news_next = driver.find_element(By.CSS_SELECTOR, ".tensor_ru-Index__block4-content.tensor_ru-Index__card  .tensor_ru-link")
	assert news_next.text == tensor_button_text
	news_next.click()
	time.sleep(5)
	#Проверки на тензор ру О компании

	assert driver.title == tensor_site_about_title, "Не верный заголовок"
	assert driver.current_url == tensor_site_about, "Не верный сайт"
	time.sleep(5)





finally:
	driver.quit()