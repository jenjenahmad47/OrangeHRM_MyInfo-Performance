import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAuth(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_add_employee(self): 
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[type=submit]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[normalize-space()='Add Employee']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Abu")
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Bakar")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)     
       
    def tearDown(self): 
        self.driver.close()

unittest.main()