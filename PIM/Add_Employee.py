import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestMenuPIM(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_add_employee_positive(self): 
        driver = self.driver

        # Proses Akses Website
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        time.sleep(3)

        # Proses Login
        driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[type=submit]").click()
        time.sleep(5)

        # Proses Add Employee First Name dan Last Name di isi
        driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click() # Klik Klik menu PIM pada sidebar
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[normalize-space()='Add Employee']").click() # Klik menu add employee
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Abu") # isi kolom First Name
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Bakar") # isi kolom Last Name
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click() # Klik button save
        time.sleep(3)

    def test_b_add_employee_negative(self): 
        driver = self.driver

        # Proses Akses Website
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        time.sleep(3)

        # Proses Login
        driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[type=submit]").click()
        time.sleep(5)

        # Proses Add Employee First Name Kosong
        driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click() # Klik Klik menu PIM pada sidebar
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[normalize-space()='Add Employee']").click() # Klik menu add employee
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("") # Kosongkan kolom First Name
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Bakar") # Kosongkan kolom Last Name
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click() # Klik button save
        time.sleep(3) 
       
    def tearDown(self): 
        self.driver.close()

unittest.main()