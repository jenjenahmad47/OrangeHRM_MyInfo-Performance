import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from lib2to3.pgen2 import driver
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.chrome.service import Service as ChromeService

class CaseLogin(unittest.TestCase):

    def setUp(self) :
        self.openbrowser = webdriver.Chrome(ChromeDriverManager().install())

        #Test Step Skenario Search all data
        #Buka URL https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
        #Input username : Admin
        #Input password : admin123
        #Klik button login
        #Klik Menu Admin
        #Klik button Search

    def test_a_login_positive(self):
        browser = self.openbrowser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        browser.maximize_window()
        time.sleep(5)

        browser.find_element(By.NAME, "username").send_keys("admin") #penulisan admin bisa menggunakan capslock
        time.sleep(1)
        browser.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(1)
        browser.find_element(By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(2)        
    
    def tearDown(self) :
        self.browser.close()

if __name__ == '__main__':
    unittest.main()

