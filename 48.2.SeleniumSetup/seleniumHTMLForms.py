from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"Users\\SHAHEERA\\Downloads\\chromedriver"
driver = webdriver.Chrome()
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element("name", "fName")
first_name.send_keys("Shaheera")
last_name = driver.find_element("name" , "lName")
last_name.send_keys("Noman")
email = driver.find_element("name", "email")
email.send_keys("shaheeranoman889@gmail.com")

submit = driver.find_element("css selector", "form button")
submit.click()
time.sleep(6)

# driver.close()
# driver.quit()
