from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.lucky-cement.com/")
lucky = response.text
soup = BeautifulSoup(lucky, "html.parser")

# title_name = soup.find("h1", class_="site-logo logo")
# print(title_name.getText)

# logo = soup.find("img")
# print(logo.getText)

# email = soup.find("a")
# print(email.getText)

# ph_num = soup.find("i")
# print(ph_num)

# Find all <i> elements with class "fa-phone"
phone_icons = soup.find_all("i", class_="fa-phone")

# Extract and print the text content of each <i> element
for phone_icon in phone_icons:
    phone_number = phone_icon.find_next_sibling(text=True).strip()
    print(phone_number)