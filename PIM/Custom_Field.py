import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestMenuPIM(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_a_add_Add_Custom_Field_Positive(self): 
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

        # Proses Add Custom Field
        driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click() # Klik menu PIM pada sidebar
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item']").click() # Klik dropdown configuration
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[normalize-space()='Custom Fields']").click() # Klik menu "custom fields"
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click() # Klik button +Add
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input").send_keys("Department") # isi kolom field name
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div[2]/i").click() # klik kolom type
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[2]/div[2]/span").click() # pilih type
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/i").click() # klik kolom screen
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[2]/span").click() # pilih screen
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@type='submit']").click() # Klik Button save
        time.sleep(10)
    
    def test_b_add_Add_Custom_Field_Negative(self): 
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

        # Proses Add Custom Field
        driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click() # Klik menu PIM pada sidebar
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[@class='oxd-topbar-body-nav-tab-item']").click() # Klik dropdown configuration
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[normalize-space()='Custom Fields']").click() # Klik menu "custom fields"
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click() # Klik button +Add
        time.sleep(3)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/input").send_keys("") # kosongkan kolom field name
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div[2]/i").click() # klik kolom type
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div[2]/div[1]").click() # kosongkan kolom type
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[1]/div[2]/i").click() # klik kolom screen
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]").click() # kosongkan kolom screen
        time.sleep(5)
        driver.find_element(By.XPATH, "//button[@type='submit']").click() # Klik Button save
        time.sleep(10)
       
    def tearDown(self): 
        self.driver.close()

unittest.main()

