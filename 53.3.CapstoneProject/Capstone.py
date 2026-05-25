from bs4 import BeautifulSoup
import requests

header = {
    "Accept_Language" : "en-US,en;q=0.9",
    "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
    }

response = requests.get("https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22north%22%3A37.842914%2C%22south%22%3A37.707608%2C%22east%22%3A-122.32992%2C%22west%22%3A-122.536739%7D%2C%22mapZoom%22%3A12%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22priorityscore%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22min%22%3A1000%2C%22max%22%3A6000%7D%2C%22price%22%3A%7B%22min%22%3A194434%2C%22max%22%3A1166604%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%2C%22category%22%3A%22cat1%22%2C%22pagination%22%3A%7B%7D%7D",
       headers=header)

data = response.text
# zillow = response.text
# print(zillow)

soup = BeautifulSoup(data, "html.parser")
# print(zillow)
