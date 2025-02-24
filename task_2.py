# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
user_login = '89407968838940796883NT'
user_password = 'Ntcn123'
online_site = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.saby.ru/'
online_title = 'Вход в личный кабинет'
exosted = 'В этой папке нет сообщений'
online_dialoge_site = 'https://fix-online.saby.ru/page/dialogs'
sms_text = 'Личное сообщение по бизнесу'


try:
	driver.get(online_site)
	time.sleep(5)
	assert driver.current_url == online_site, "Не верный сайт"
	assert driver.title == online_title, "Не верный заголовок"
	login = driver.find_element(By.CSS_SELECTOR, '.controls-Field.js-controls-Field.controls-InputBase__nativeField.controls-InputBase__nativeField_caretFilled')
	login.click()
	login.send_keys(user_login, Keys.ENTER)
	#controls-Field js-controls-Field controls-InputBase__nativeField controls-Password__nativeField_caretFilled controls-Password__nativeField_caretFilled_theme_default controls-InputBase__nativeField_hideCustomPlaceholder
	password = driver.find_element(By.CSS_SELECTOR, '.controls-Password__nativeField_caretFilled_theme_default')
	time.sleep(3)
	password.send_keys(user_password, Keys.ENTER)
	time.sleep(5)

	#С разводящей онлайн переходим в контакты
	reeestr = driver.find_element(By.XPATH, "//*[contains(text(),'Контакты')]")
	reeestr.click()
	time.sleep(5)
	reestr_click = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle.NavigationPanels-SubMenu__title-with-separator.NavigationPanels-Accordion__prevent-default')
	reestr_click.click()
	time.sleep(5)

	#В реестре сообщений выбираем пользователя
	assert driver.current_url == online_dialoge_site
	plus_message = driver.find_element(By.CSS_SELECTOR, '.controls-BaseButton__icon.controls-icon_size-m.controls-icon.icon-RoundPlus')
	plus_message.click()
	time.sleep(5)
	catcher = driver.find_element(By.CSS_SELECTOR, '.controls-TileView__item.controls-ListView__itemV.js-controls-ListView__editingTarget.controls-TileView__item_unscalable.ws-flex-grow-1.controls-TileView__item_spacingLeft_s')
	actions = ActionChains(driver)
	actions.move_to_element(catcher).perform()
	actions.context_click(catcher).perform()
	catcher.click()
	time.sleep(5)

	#Создаем, отправляем и переоткрываем сообщение
	message_stroke = driver.find_element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph.textEditor_Viewer__Paragraph_empty')
	message_stroke.click()
	message_stroke.send_keys(sms_text)
	time.sleep(2)
	sender_btn = driver.find_element(By.CSS_SELECTOR, '.controls-BaseButton__icon.controls-icon_size-s.controls-icon.icon-BtArrow')
	sender_btn.click()
	time.sleep(5)
	message_in_row = driver.find_element(By.CSS_SELECTOR, '.msg-entity-text.msg-entity_font_croppless.richEditor_richContentRender_fontSize-m_theme-default.controls_RichEditor_theme-default.richEditor_richContentRender_theme-default')
	assert message_in_row.text == sms_text
	message_in_row.click()
	time.sleep(2)

	#Удаляем сообщение
	delete_btn = driver.find_element(By.CSS_SELECTOR, '.icon-Erase.controls-icon')
	delete_btn.click()
	time.sleep(2)

	#Проверяем что список пустой благодаря заглушке в пустом представлении
	empty_list = driver.find_element(By.CSS_SELECTOR, '.hint-Template__text_message.hint-Template__text_message_m')
	assert empty_list.text == exosted
	time.sleep(2)

finally:
	driver.quit()

