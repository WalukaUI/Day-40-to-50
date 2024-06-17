from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# get_atag_withoutclass = driver.find_elements(By.XPATH,
#                                             value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

count_id = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# ev_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
print(count_id.text)