import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(2)
driver.find_element(By.NAME, "username").send_keys("Admin") 
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("admin123") 
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "[type=submit]").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a").click() #Click Menu Recruitment 
time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='Vacancies']").click() #ClickVacancies
time.sleep(3)
driver.find_element(By.XPATH, "//div[9]//div[1]//div[6]//div[1]//button[2]//i[1]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//div[4]//div[1]//div[1]//label[1]//span[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)