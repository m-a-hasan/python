from apscheduler.schedulers.background import BackgroundScheduler
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

sched_5_sec = BackgroundScheduler()
sched_5_min = BackgroundScheduler()

driver.get("https://orteil.dashnet.org/experiments/cookie/")
money = driver.find_element(By.CSS_SELECTOR, "#money")
cookie = driver.find_element(By.CSS_SELECTOR, "#cookie")

game_on = True


def upgrade():
    items = driver.find_elements(By.CSS_SELECTOR, "#store b")
    try:
        for item in reversed(items):
            price = item.text.split(" - ")
            if len(price) == 2:
                payment = int(price[1].replace(",", ""))
                wallet = int(money.text.replace(",", ""))
                if wallet > payment:
                    item.click()
                    break
    except:
        pass


def game_over():
    global game_on
    game_on = False
    print(f"Total cookies: {money.text}")
    sched_5_sec.shutdown(wait=False)
    sched_5_min.shutdown(wait=False)
    driver.quit()


# seconds can be replaced with minutes, hours, or days
sched_5_sec.add_job(upgrade, 'interval', seconds=5)
sched_5_sec.start()

sched_5_min.add_job(game_over, 'interval', seconds=300)
sched_5_min.start()

while game_on:
    cookie.click()
