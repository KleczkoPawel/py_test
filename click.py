from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
import time
from selenium.webdriver.firefox.options import Options

#options = Options()
#options.binary_location = r"/home/firefox/firefox-bin"

opts = FirefoxOptions()
opts.add_argument("--headless")

""" profile = webdriver.FirefoxProfile()
default_download_path = profile['browser.download.dir']
print(default_download_path) """

profile = webdriver.FirefoxProfile(firefox_profile=profile)
profile.set_preference("browser.download.dir", "/nowa/lokalizacja")
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")

driver = webdriver.Firefox(options=opts, firefox_binary="/home/firefox/firefox-bin")
driver.get("https://www.cvedetails.com/vulnerability-list/vendor_id-12752/product_id-25450/Mongodb-Mongodb.html")

element = driver.find_element(By.LINK_TEXT, "Download Results")

element.click()
time.sleep(5)
driver.quit()