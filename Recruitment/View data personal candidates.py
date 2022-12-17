import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "[type=submit]").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div.orangehrm-container > div > div > div:nth-child(4) > div > div > div.card-header-slot > div.card-item.card-header-slot-content.--right > div > div > button:nth-child(1)").click()
time.sleep(5)

