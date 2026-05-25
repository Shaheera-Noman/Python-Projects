import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import lxml

url = "https://www.noon.com/"

product_links = []

for x in range(1,187):
    r = requests.get(f"https://www.noon.com/uae-en/search/?limit=50&originalQuery=mobile%20smartphone&page={x}&q=mobile%20smartphone&searchDebug=false&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc")

# r = requests.get(f"https://www.noon.com/uae-en/search/?limit=50&originalQuery=mobile%20smartphone&page=1&q=mobile%20smartphone&searchDebug=false&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc")
    soup = BeautifulSoup(r.content, "html.parser")
    spans = soup.find_all('span', class_='sc-5c17cc27-0 eCGMdH wrapper productContainer')
    for span in spans:
        links = span.finad_all('a')
        for link in links:
            productlinks = url + link['href']
            product_links.append(productlinks)
print(len(product_links))
# print(soup)

# noon = r.text
# soup = BeautifulSoup(noon, 'htlm.parser')
# print(soup)

# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://www.amazon.com/")
# response.raise_for_status()
# # amazon = response.text
# # soup = BeautifulSoup(amazon, "html.parser")
# soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import datetime

# url = "https://www.amazon.com/"

# product_links = []

# # for x in range(1,20):
# #     r = requests.get(f"https://www.amazon.com/s?k=mobile+phone&page={x}&crid=2KYL2RF8F3JXE&qid=1705659883&sprefix=mobile+phone%2Caps%2C266&ref=sr_pg_{x}")

# r = requests.get(f"https://www.amazon.com/s?k=mobile+phone&page=2&crid=2KYL2RF8F3JXE&qid=1705659883&sprefix=mobile+phone%2Caps%2C266&ref=sr_pg_2")
# soup = BeautifulSoup(r.content, "html.parser")
# # print(soup)

# spans = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
# for span in spans:
#     links = soup.find_all('a')
#     for link in links:
#         productlinks = url + link['href']
#         product_links.append(productlinks)

# # Print or process the product_links as needed
# # print(product_links)
        

# # ------  DARAZ ------- #
        
# url = "https://www.daraz.com/"

# product_links = []

# r = requests.get(f"https://www.daraz.pk/catalog/?_keyori=ss&clickTrackInfo=textId--8106960466929852021__abId--None__pvid--71b428a2-7767-445d-b27e-0ef69f314b17__matchType--1__abGroup--None__srcQuery--mobile%20phones__spellQuery--mobile%20phones__ntType--nt-common&from=suggest_normal&page=1&q=mobile%20phones&spm=a2a0e.home.search.1.35e340761eRLqL&sugg=mobile%20phones_0_1")
# soup = BeautifulSoup(r.content, "html.parser")
# # print(soup)

# spans = soup.find_all(class_='description--H8JN9')
# for span in spans:
#      links = soup.find_all('a')
#      for link in links:
#         productlinks = url + link['href']
#         print(productlinks)