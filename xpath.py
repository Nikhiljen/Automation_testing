# Import all necessary module

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create a service object

ser_obj = Service("/home/nikhil-95/Drivers/chromedriver")

# Create a webdriver object
driver = webdriver.Chrome(service = ser_obj)

# lunch browser using .get()
driver.get("https://automationpractice.com/index.php")

# maximize browser windows using maximize_window method
driver.maximize_window()


# xpath absolute path
#driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-Shirts")
#driver.find_element(By.XPATH,"//*[@id='searchbox']/button").click()


# or and condition
#driver.find_element(By.XPATH,"//input[@id='search_query_top' or @placeholder='Search']").send_keys("T-Shirts")
#driver.find_element(By.XPATH,"//button[@name='submit_search' and @type='submit']").click()



#continue[] and starts-with[]
driver.find_element(By.XPATH,"//input[contains(@id,'search_query_top')]").send_keys("T-shirts")
#driver.find_element(By.XPATH,"//button[@name='submit_search' and @type='submit']").click()


