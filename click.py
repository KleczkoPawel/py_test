from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

#options = Options()
#options.binary_location = r"/home/firefox/firefox-bin"
driver = webdriver.Firefox(firefox_binary="/home/firefox/firefox-bin")
driver.get("https://www.cvedetails.com/vulnerability-list/vendor_id-12752/product_id-25450/Mongodb-Mongodb.html")
element = driver.find_element(By.XPATH, '//button[text()="Download Results"]')
element.click()
driver.quit()