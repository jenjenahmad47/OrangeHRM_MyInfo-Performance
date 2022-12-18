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
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button").click()
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input").send_keys("") # First Name
time.sleep(5)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[3]/div[2]/input").send_keys("") # Last Name
time.sleep(5)
driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']").click() # vacancy
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[2]/div[2]/span").click() # isi vacancy
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input").send_keys ("daejunyoung@gmail.com") # Email
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input").send_keys("09481938920") # Contact Number
time.sleep(5)
driver.find_element(By.XPATH, "//input[@placeholder='Enter comma seperated words...']").send_keys("QA, Testing") # keyword
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/div/div[2]/div/div[2]/div/div[1]/input").click() # date of application
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div[17]/div").click() # pilih tanggal
time.sleep(2)
driver.find_element(By.XPATH, "//textarea[@placeholder='Type here']").send_keys("I have experience") # notes
time.sleep(3)
driver.find_element(By.XPATH, "//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']").click() # Consent to keep data
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]").click() #save
time.sleep(5)
