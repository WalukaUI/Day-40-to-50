from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(3)
driver.find_element(By.ID, value="langSelect-EN").click()

time.sleep(3)
num = 1000

driver.find_element(By.ID, value="bigCookie").click()
get_marks = driver.find_element(By.ID, value="cookies").text.split(" ")[0]
marks = int(get_marks)

productids = []
prices = []

while marks < num:
    driver.find_element(By.ID, value="bigCookie").click()
    marks = int(driver.find_element(By.ID, value="cookies").text.split(" ")[0])
    if marks % 100 == 0:
        items = driver.find_elements(by=By.CSS_SELECTOR, value="#store #products .unlocked .content .price")
        if len(items) > 0:
            for x in items:
                productids.append(x.get_attribute("id"))
                prices.append(int(x.text))
        num = prices.index(min(prices))
        min_price = min(prices)
        while marks > min_price:
            driver.find_element(By.ID, value="bigCookie").click()
            time.sleep(0.1)
            driver.find_element(By.ID, value=f"product{num}").click()
            marks = int(driver.find_element(By.ID, value="cookies").text.split(" ")[0])
        productids = []
        prices = []







