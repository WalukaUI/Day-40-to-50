from selenium import webdriver
from selenium.webdriver.common.by import By
# keep browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/dp/B08NB1VGBK/ref=sbl_dpx_kitchen-electric-cookware_B08WCLJ7JG_0?th=1")
dollar_price = driver.find_element(By.CLASS_NAME, value="a-span12")
print(dollar_price.text)
print("mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
get_atag_withoutclass = driver.find_element(By.XPATH, value='//*[@id="customerReviewsAttribute_feature_div"]/div/div[2]/div[1]/div/div/div[1]/div/span')
print(get_atag_withoutclass.text)
# close only tab
driver.close()

# close chrome
# driver.quit()
