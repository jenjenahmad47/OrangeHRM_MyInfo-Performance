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

# Opens My Info Menu > Personal Details
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewMyDetails")
time.sleep(3)

# Input First Name, Middle Name, Last Name, and Nickname
driver.find_element(By.NAME, "firstName").send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
driver.find_element(By.NAME, "firstName").send_keys("Matthew")
time.sleep(3)
driver.find_element(By.NAME, "middleName").send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
driver.find_element(By.NAME, "middleName").send_keys("Thomas")
time.sleep(3)
driver.find_element(By.NAME, "lastName").send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
driver.find_element(By.NAME, "lastName").send_keys("Spiranovic")
time.sleep(3)
Nickname=driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]")
ClearNickname=Nickname.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
InputNickname=Nickname.send_keys("Jenjen")
time.sleep(3)

# Input Employee ID and Other ID
EmpID=driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[1]/div[1]/div[2]/input[1]")
ClearEmpID=EmpID.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
InputEmpID=EmpID.send_keys("471147")
time.sleep(3)
OtherID=driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]")
ClearOtherID=OtherID.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
InputOtherID=OtherID.send_keys("999999")
time.sleep(3)

# Input Driver License Number and License Expire Date
DrivLicNum=driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[2]/input[1]")
ClearDrivLicNum=DrivLicNum.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
InputDrivLicNum=DrivLicNum.send_keys("AXX19872-988564")
time.sleep(3)
LicExpireDate=driver.find_element(By.XPATH, "//input[@placeholder='yyyy-mm-dd']")
LicExpireDate.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
LicExpireDate.send_keys("2025-12-18")
time.sleep(3)


SSNNum=driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[3]/div[1]/div[1]/div[2]/input[1]")
ClearSSNNum=SSNNum.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
InputSSNNum=SSNNum.send_keys("10987654321")
time.sleep(3)
SINNum=driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[1]")
ClearSINNum=SINNum.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
InputSINNum=SINNum.send_keys("10987654321")
time.sleep(3)

# Input Nationality
nationality = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")))
for x in range(83):nationality.send_keys(Keys.ARROW_DOWN)
#nationality.send_keys(Keys.RETURN)
time.sleep(2)

# Input Marital Status
marital = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")))
for y in range(3):marital.send_keys(Keys.ARROW_DOWN)
time.sleep(2)

# Input Date of Birth, Gender, Military Status, and Smoker Checkbox
DateOfBirth=driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
DateOfBirth.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
DateOfBirth.send_keys("1999-08-07")
time.sleep(2)
FemaleGender=driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/label[1]/span[1]").click()
time.sleep(2)
MaleGender=driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/label[1]/span[1]").click()
time.sleep(2)
MilitaryService=driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[1]/div[1]/div[2]/input[1]")
MilitaryService.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
MilitaryService.send_keys("No")
time.sleep(2)
Smoking=driver.find_element(By.XPATH, "//div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[1]/div[2]/div[1]/div[2]/div[1]/label[1]/span[1]/i[1]").click()
time.sleep(2)

# Save the changes
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[5]/button[1]").click()
time.sleep(8)
# Close the Chrome
driver.close()

print("\nTest case successfully completed")
