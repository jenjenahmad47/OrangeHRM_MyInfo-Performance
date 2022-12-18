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
driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
time.sleep(8)
driver.find_element(By.CSS_SELECTOR, ".oxd-input.oxd-input--focus").send_keys("Quality Assurance")
time.sleep(4)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div/div[2]/div/div[2]/div[17]/span").click()
time.sleep(8)
driver.find_element(By.XPATH, "//textarea[@placeholder='Type description here']").send_keys("Kualifikasi")
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div/input").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/div/div[2]/div[4]").click()
time.sleep(8)
driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--focus']").send_keys("3")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(10)