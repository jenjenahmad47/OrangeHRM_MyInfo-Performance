from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time  

print("Test case now started")


options = webdriver.ChromeOptions()
options.add_argument("start-maximized");
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Opens Orange's login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)

# Login session. Input Username and Password, then login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.CLASS_NAME, "oxd-button").click()
time.sleep(3)

# Opens Performance
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/performance/searchEvaluatePerformanceReview")
time.sleep(5)

# Input Employee Name (Apologize, it's difficult to access the autocomplete text's path.)

#EmployeeName=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type for hints...']"))).send_keys('Anthony Nolan')
#time.sleep(5)
#Name = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='oxd-autocomplete-text-input'])"))).send_keys(Keys.ARROW_DOWN)
#elusive_el = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-autocomplete-text-input--after")))
#print(elusive_el.get_attribute('outerHTML'))
#name_option = elusive_el.find_element(By.XPATH, "//div[text()='Anthony Nolan']")
#name_option.click()
#print('selected Anthony')

#InputName=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type for hints...']"))).send_keys('ant')
#time.sleep(2)
#Name = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='oxd-autocomplete-text-input'])")))
#time.sleep(2)
#Name.send_keys(Keys.ARROW_DOWN)
#time.sleep(2)

# Input Job Title
JobTitle = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")))
for x in range(4):JobTitle.send_keys(Keys.ARROW_DOWN)
time.sleep(2)

# Input Sub Unit
SubUnit = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")))
for y in range(4):SubUnit.send_keys(Keys.ARROW_DOWN)
time.sleep(2)

# Input Include
Include = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='oxd-select-text-input'])[3]")))
for z in range(3):Include.send_keys(Keys.ARROW_DOWN)
time.sleep(2)

# Input Review Status
ReviewStatus = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='oxd-select-text-input'])[4]")))
for xx in range(3):ReviewStatus.send_keys(Keys.ARROW_DOWN)
time.sleep(2)

# From Date
FromDate=driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[1]")
FromDate.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
FromDate.send_keys("2022-12-01")
time.sleep(3)

# To Date
ToDate=driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-mm-dd'])[2]")
ToDate.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
ToDate.send_keys("2022-12-31")
time.sleep(3)

# Save the changes
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(8)

# Close the Chrome
driver.close()

print("\nTest case successfully completed")