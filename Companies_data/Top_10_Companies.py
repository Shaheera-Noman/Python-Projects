import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html

URL = "https://www.forbesindia.com/article/explainers/top-10-largest-companies-world-market-cap/86341/1"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
# tree = html.fromstring(website_html)
# print(soup.prettify())

companies =  soup.find_all(name="a", rel="nofollow")
# Use slice to get the first 10 elements
first_10_companies = companies[:14]

# Print the first 10 companies
for company in first_10_companies:
    # print(company.get("href"))
    print(company.text)

# ceo_name =  soup.find_all(name="h2", string="Current CEO:")
# ceo_name = soup.find_all('h2 + ul li:contains("Current CEO:")').split(":")[1].strip()
# first_10_ceo = ceo_name[:14]
# for ceo in first_10_ceo:
#     print(ceo.text)

# print(ceo_name)
