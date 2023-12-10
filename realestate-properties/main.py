import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://appbrewery.github.io/Zillow-Clone/")

addresses = driver.find_elements(By.CSS_SELECTOR, ".StyledPropertyCardDataWrapper a")
address_1 = [a.text for a in addresses]
address_2 = [a.split("|") for a in address_1]
address_3 = [a[1] if len(a) == 2 else a[0] for a in address_2]
address = [a.strip() for a in address_3]

href = driver.find_elements(By.CSS_SELECTOR, ".StyledPropertyCardDataWrapper [href]")
link = [h.get_attribute('href') for h in href]

prices = driver.find_elements(By.CSS_SELECTOR, ".PropertyCardWrapper__StyledPriceLine")
price_1 = [p.text for p in prices]
price_2 = [p.split("+") for p in price_1]
price_3 = [p[0] for p in price_2]
price_4 = [p.split("/") for p in price_3]
price = [p[0] for p in price_4]

driver.quit()

# Fill out the form

questionnaire = webdriver.Chrome(options=chrome_options)
questionnaire.get("https://docs.google.com/forms/d/e/1FAIpQLSdK3BZiL-frRerBJ0zpOWcJ9JzVz6LPYH-HRe-k3YPyfqMA3g/viewform?usp=sf_link")

for i in range(len(price)):
    time.sleep(5)
    questions = questionnaire.find_elements(By.CSS_SELECTOR, ".rFrNMe.k3kHxc.RdH0ib.yqQS1.zKHdkd input")
    questions[0].send_keys(address[i])
    questions[1].send_keys(price[i])
    questions[2].send_keys(link[i])

    time.sleep(2)
    submit = questionnaire.find_element(By.CSS_SELECTOR, ".l4V7wb.Fxmcue")
    submit.click()

    time.sleep(5)
    another = questionnaire.find_element(By.LINK_TEXT, "Submit another response")
    another.click()

questionnaire.quit()
