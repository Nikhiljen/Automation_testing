# Import all necessary module

from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a webdriver object
driver = webdriver.Chrome(executable_path="/home/nikhil-95/Drivers/chromedriver")
# lunch browser using .get()
driver.get("https://automationpractice.com/index.php")
# maximize browser windows using maximize_window method
driver.maximize_window()

driver.find_element_by_xpath("//input[contains(@id,'search_query_top')]").send_keys("T-shirts")
driver.find_element(By.XPATH, "//button[@name='submit_search' and @type='submit']").click()
