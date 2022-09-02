# title,current_url,page_source
from selenium import webdriver
# from selenium.webdriver.common.by import By

# Create a webdriver object
driver = webdriver.Chrome(executable_path="/home/nikhil-95/Drivers/chromedriver")

# lunch browser using .get()
driver.get("https://automationpractice.com/index.php")

# maximize browser windows using maximize_window method
driver.maximize_window()

print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.quit()
