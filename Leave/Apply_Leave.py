import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestAuth(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_Apply_Leave(self): 
        driver = self.driver

        # Proses Akses Website
        driver.get("https://opensource-demo.orangehrmlive.com/")
        driver.maximize_window()
        time.sleep(3)

        #Proses Login
        driver.find_element(By.NAME,"username").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"[type=submit]").click()
        time.sleep(5)

        # Proses Mengakses Halaman Apply Leave
        driver.find_element(By.XPATH, "//span[normalize-space()='Leave']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[normalize-space()='Apply']").click()
        time.sleep(5)

        # Proses Mengisi data Kolom Leave Type
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[1]/div[2]/i").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(5)
        
        # Proses Mengisi data Kolom From Date
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[1]/i").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[27]/div").click()
        time.sleep(5)

        # Proses Mengisi data Kolom To Date
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[1]/i").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div[28]/div").click()
        time.sleep(5)

        # Proses Mengisi data Kolom Partial Days
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div[1]/div[2]/i").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div[2]/div[2]/span").click()
        time.sleep(5)

        # Proses Mengisi data Kolom Duration
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div[1]/div[2]/i").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(5)

        # Proses Mengisi data Kolom Comments
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div/div/div[2]/textarea").send_keys("Wedding Agreement")
        time.sleep(5)

        # Proses Save
        driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[5]/button").click()
        time.sleep(5)
       
    def tearDown(self): 
        self.driver.close()

unittest.main()
