from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")


fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
btn = driver.find_element(By.XPATH, value="/html/body/form/button")

fname.send_keys("Python")
lname.send_keys("test")
email.send_keys("Python@yahoo.com")
btn.click()

