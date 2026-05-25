from selenium import webdriver


chrome_driver_path = "\\Users\\SHAHEERA\\Downloads\\chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.Chrome()

driver.get("https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8/ref=sr_1_3?crid=1P8LPCHAXK3BU&keywords=instant%2Bpot%2Bduo%2Bevo%2Bplus%2B9-in-1%2Belectric%2Bpressure%2Bcooker%2C%2Bsterilizer%2C%2Bslow%2Bcooker%2C%2Brice%2Bcooker%2C%2Bgrain%2Bmaker%2C%2Bsteamer%2C%2Bsaute%2C%2Byogurt%2Bmaker%2C%2Bsous%2Bvide%2C%2Bbake%2C%2Band%2Bwarmer%2C%2B6%2Bquart%2C%2B10%2Bprograms&qid=1702008935&sprefix=instant%2Bpot%2Bduo%2Bevo%2Bplus%2B9-in-1%2Belectric%2Bpressure%2Bcooker%2C%2Bsterilizer%2C%2Bslow%2Bcooker%2C%2Brice%2Bcooker%2C%2Bgrain%2Bmaker%2C%2Bsteamer%2C%2Bsaute%2C%2Byogurt%2Bmaker%2C%2Bsous%2Bvide%2C%2Bbake%2C%2Band%2Bwarmer%2C%2B6%2Bquart%2C%2B10%2Bprograms%2Caps%2C246&sr=8-3&th=1")
price = driver.find_element("id", "taxInclusiveMessage")
print(price.text)



# driver.close()
driver.quit()


