
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv
import time

load_dotenv()

def login_and_navigate():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    CHROMEDRIVER_PATH = "/usr/bin/chromedriver"
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://io-fund.com/login")
    time.sleep(2)

    driver.find_element(By.ID, "Email").send_keys(os.getenv("dobes.jiri@gmail.com"))
    driver.find_element(By.ID, "Password").send_keys(os.getenv("7836578365"))
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(3)
    driver.get("https://wire.io-fund.com/advanced/categories/market-signals")
    time.sleep(3)

    return driver
