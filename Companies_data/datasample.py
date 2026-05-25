import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

URL = "https://www.forbesindia.com/article/explainers/top-10-largest-companies-world-market-cap/86341/1"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

# Create a list to store company names
companies_list = []

# Find all company names and add them to the list
companies = soup.find_all(name="a", rel="nofollow")
for index, company in enumerate(companies[2:13], start=1):
    company_name = company.text.strip()
    companies_list.append({"Serial Number": index, "Company": company_name})

# Create a DataFrame from the list
company_df = pd.DataFrame(companies_list)

# Left-align the "Company" column
company_df["Company"] = company_df["Company"].apply(lambda x: x.ljust(20))

# Print the DataFrame with a box
print(tabulate(company_df, headers="keys", tablefmt="fancy_grid", showindex=False))




