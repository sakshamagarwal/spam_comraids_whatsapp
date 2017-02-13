from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import sys
import time

def wait_for_qr_scan(driver, delay) :
	try :
	    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'side')))
	except TimeoutException :
	    # print("page not loaded...\nexiting...")
	    wait_for_qr_scan(driver, delay)

if __name__ == "__main__" :

	CHROME_DRIVER = os.getcwd() + os.path.sep + "chromedriver"
	WHATAPP_WEB_URL = "http://web.whatsapp.com"
	WHATAPP_GROUP_KW = "Comraids"

	driver = webdriver.Chrome(CHROME_DRIVER) # You can change the path of chromedriver here if you want
	# driver = webdriver.Firefox()  # Uncomment this if you do not have chrome/chromedriver and comment the above line

	DELAY = 5

	driver.maximize_window()
	driver.get(WHATAPP_WEB_URL)

	print("Waiting for you to scan the qr code...")
	wait_for_qr_scan(driver, DELAY)

	search_input = driver.find_element_by_tag_name("input")
	search_input.send_keys(WHATAPP_GROUP_KW)

	try:
		WebDriverWait(driver, DELAY).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.list-title')))
	except TimeoutException:
		print("Something bad happened\nexiting")
		sys.exit()

	chat_div = driver.find_element_by_css_selector("div.chat-body")
	print("REMEMBER, WITH GREAT POWER COMES GREAT RESPONSIBILITY!")
	chat_div.click()

	while True:
		print("REMEMBER, WITH GREAT POWER COMES GREAT RESPONSIBILITY!")
		print("Enter the number of times you want to spam:")
		spam_count = input()
		for i in range(spam_count):
			msg_input = driver.find_element_by_css_selector("div.input")
			for x in range(ord('a'),ord('z') + 1):
				if x != ord('e'):
					msg_input.send_keys(chr(x))
					print("REMEMBER, WITH GREAT POWER COMES GREAT RESPONSIBILITY!")
					send_button = driver.find_element_by_css_selector("button.icon.btn-icon.icon-send.send-container")
					send_button.click()
