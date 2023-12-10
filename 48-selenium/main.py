from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/NexiGo-D90-Sony_Sensors-Emergency-Assistance/dp/B0B7Y2RH9K")
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# print(f"{price_dollar.text}.{price_cent.text}")

##################################################################################################

# driver.get("https://www.python.org/")
#
# event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
#
# events = {}
#
# for n in range(len(event_times)):
#     events[n] = {
#             "time": event_times[n].text,
#             "name": event_names[n].text
#         }
#
# print(events)

#######################################################################################################

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)

#######################################################################################################

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# all_portals = driver.find_element(By.LINK_TEXT, "Community portal")
# all_portals.click()

########################################################################################################

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# search_text = driver.find_element(By.NAME, "search")
# search_text.send_keys("Python")
# search_text.send_keys(Keys.ENTER)

###########################################################################################################

driver.get("https://secure-retreat-92358.herokuapp.com/")

firstname = driver.find_element(By.NAME, "fName")
firstname.send_keys("Abid")

lastname = driver.find_element(By.NAME, "lName")
lastname.send_keys("Hasan")

email = driver.find_element(By.NAME, "email")
email.send_keys("abid_hasan@example.com")

btn = driver.find_element(By.XPATH, "//button[text()='Sign Up']")
btn.click()

# driver.quit()
