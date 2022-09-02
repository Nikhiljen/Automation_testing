# there are 4 way to write css selector
# tag id    tagname#idvalue
# tag class  tag name.class value
# tag attribute  tag name[attribute name = value]
# tag class attribute tag name.class value[attribute name = value]

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create a service object

ser_obj = Service("/home/nikhil-95/Drivers/geckodriver")

# Create a webdriver object
driver = webdriver.Firefox(service = ser_obj)

# lunch browser using .get()
driver.get("https://www.facebook.com/")

# maximize browser windows using maximize_window method
driver.maximize_window()

# tag_name#id_value
    #driver.find_element(By.CSS_SELECTOR,'input#email').send_keys("abc@gmail.com")
    #driver.find_element(By.CSS_SELECTOR,'#email').send_keys("abc@gmail.com")

#tag_name.class_value
    #driver.find_element(By.CSS_SELECTOR,'input.inputtext').send_keys("abc@gmail.com")
    #driver.find_element(By.CSS_SELECTOR,'.inputtext').send_keys("abc@gmail.com")

# tag[atrribute=attribute_value]
#driver.find_element(By.CSS_SELECTOR,'input[data-testid=royal_email]').send_keys("abc@gmail.com")

# tag.class[atrribute]
driver.find_element(By.CSS_SELECTOR,'input.inputtext[data-testid=royal_pass]').send_keys("abc@123")


