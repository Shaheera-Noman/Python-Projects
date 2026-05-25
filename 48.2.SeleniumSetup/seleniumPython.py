from selenium import webdriver


chrome_driver_path = "\\Users\\SHAHEERA\\Downloads\\chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.Chrome()

driver.get("https://www.python.org/")

# search_bar = driver.find_element("name", "q")
# print(search_bar.tag_name)
# # print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element("class", "python-logo")
# print(logo.size)

# documentation_link = driver.find_element("css_selector", ".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element("xpath", '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# audio_visual = driver.find_element("xpath", '//*[@id="container"]/li[3]/ul/li[2]/a')
# print(audio_visual.text)

# event_times = driver.find_elements("css selector", ".event-widget last")
# for time in event_times:
#  print(time.text)

event_times = driver.find_elements("css selector", ".event-widget time")
event_names = driver.find_elements("css selector", ".event-widget li a")
events = {}
# for name in event_names:
#   print(name.text)

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

# driver.close()
driver.quit()
