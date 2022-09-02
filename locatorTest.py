# Import all neccssary module

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create a service object

ser_obj = Service("/home/nikhil-95/Drivers/geckodriver")

# Create a webdriver object
driver = webdriver.Firefox(service = ser_obj)

# lunch browser using .get()
driver.get("https://demo.nopcommerce.com/")

# maximize browser windows using maximize_window method
driver.maximize_window()

# id and name locators 
#driver.find_element(By.ID, "small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
#driver.find_element(By.NAME, "q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# link text and partial link test locators

#driver.find_element(By.LINK_TEXT, "Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Regi").click()

