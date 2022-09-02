import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Create a webdriver object
driver = webdriver.Chrome(executable_path="/home/nikhil-95/Drivers/chromedriver")
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

# maximize browser windows using maximize_window method
driver.maximize_window()

# get element using xpath
alerts = driver.find_element(By.XPATH, "//input[@title='Sign in']")
alerts.click()
time.sleep(5)
#auto_alerts = driver.switch_to.alert.accept()
driver.switch_to.alert.accept()

# close window using Accept or dismiss method
#auto_alerts.accept()
#auto_alerts.dismiss()