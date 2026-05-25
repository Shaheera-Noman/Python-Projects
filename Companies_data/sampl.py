# import requests
# from bs4 import BeautifulSoup

# URL = "https://www.forbesindia.com/article/explainers/top-10-largest-companies-world-market-cap/86341/1"

# response = requests.get(URL)
# website_html = response.text

# soup = BeautifulSoup(website_html, 'html.parser')

# # Find the company name
# company_name = soup.find_all(name="a", rel="nofollow").text

# # Find the CEO name directly (assuming the structure remains consistent)
# ceo_name = soup.select_one('h2 + ul li:contains("Current CEO:")').text.split(":")[1].strip()

# print(f"Company Name: {company_name}")
# print(f"CEO: {ceo_name}")

import requests
from bs4 import BeautifulSoup

URL = "https://www.forbesindia.com/article/explainers/top-10-largest-companies-world-market-cap/86341/1"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

companies = soup.find_all(name="a", rel="nofollow")
first_10_companies = companies[:14]

# Print the first 10 companies
for company in first_10_companies:
    print(company.text)

# Find the Current CEO information for each company
for heading in soup.find_all("h2"):
    company_name = heading.text.strip()
    ceo_li = heading.find_next("li", string="Current CEO:")

    if ceo_li:
        ceo_name = ceo_li.text.replace("Current CEO:", "").strip()
        print(f"Company: {company_name}, Current CEO: {ceo_name}")
    else:
        print(f"Company: {company_name}, Current CEO information not found")









