import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TimesheetEmployee(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_positif_add_employee(self): 
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[type=submit]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[normalize-space()='Time']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("Saeid")
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@class='oxd-autocomplete-option']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        
    def test_negatif_add_not_employee(self): 
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[type=submit]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[normalize-space()='Time']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys("anto")
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@class='oxd-autocomplete-option']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

    def test_negatif_add_blank_employee(self): 
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[type=submit]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[normalize-space()='Time']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").send_keys(" ")
        time.sleep(5)
        driver.find_element(By.XPATH,"//div[@class='oxd-autocomplete-option']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)

    def test_view_employee(self): 
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[type=submit]").click()
        time.sleep(5)   
        driver.find_element(By.XPATH, "//span[normalize-space()='Time']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,"(//button[@type='button'][normalize-space()='View'])").click()
        time.sleep(3)

    def tearDown(self): 
        self.driver.close()

unittest.main()