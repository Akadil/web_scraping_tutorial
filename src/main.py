from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set the path to the Chromedriver
DRIVER_PATH = '/Users/akadilkalimoldayev/chromedriver/chromedriver'

# configure a connection to driver
service = Service(executable_path=DRIVER_PATH)
options = Options()
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1200")

# Initialize the Chrome driver
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the URL
driver.get('https://www.nintendo.com/')

# print(driver.page_source)
print(driver.capabilities)

time.sleep(5)
# It's a good practice to close the browser when done
driver.quit()