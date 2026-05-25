from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "\\Users\\SHAHEERA\\Downloads\\chromedriver"
driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# num_of_articles = driver.find_element("css selector", "#articlecount a:nth-child(2)")
num_of_articles = driver.find_element("css selector", "#articlecount a")
# num_of_articles.click()

portals = driver.find_element(By.LINK_TEXT, "Portals")
# portals.click()
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
time.sleep(6)

# print(num_of_articles.text)
