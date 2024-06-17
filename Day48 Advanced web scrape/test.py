from selenium import webdriver
from selenium.webdriver.common.by import By

# keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
get_atag_withoutclass = driver.find_elements(By.XPATH,
                                            value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li')

new_lst = {}

ev_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
ev_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
for x in range(len(ev_time)):
    new_lst[x] = {"time": ev_time[x].text, "name": ev_name[x].text}

print(new_lst)




