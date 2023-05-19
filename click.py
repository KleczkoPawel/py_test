from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
import time


#options = Options()
#options.binary_location = r"/home/firefox/firefox-bin"
opts = FirefoxOptions()
opts.add_argument("--headless")

driver = webdriver.Firefox(options=opts, firefox_binary="/home/firefox/firefox-bin")
driver.get("https://www.cvedetails.com/vulnerability-list/vendor_id-12752/product_id-25450/Mongodb-Mongodb.html")

element = driver.find_element(By.LINK_TEXT, "Download Results")

element.click()
time.sleep(5)
driver.quit()