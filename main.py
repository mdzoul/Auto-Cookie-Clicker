from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

s = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=s)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, 'cookie')

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()
    if time.time() > timeout:
        buyable = []
        store = driver.find_elements(By.CSS_SELECTOR, value="#store div")
        for item in store[:-1]:
            if item.get_attribute('class') != "grayed":
                buyable.append(item)
        buyable[-1].click()
        timeout = time.time() + 5
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, value="cps").text
        print(cookie_per_s)
        break

