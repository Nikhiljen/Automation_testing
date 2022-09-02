from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a webdriver object
driver = webdriver.Chrome(executable_path="/home/nikhil-95/Drivers/chromedriver")

# lunch browser using .get()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

# maximize browser windows using maximize_window method
driver.maximize_window()

# Conditional commands

# is_displayed
register = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("After displayed.....")
print(register.is_displayed())

# is_enabled
register_enabled = driver.find_element(By.XPATH, "//button[@class='button-1 search-box-button']")
print("After enabled.....")
print(register.is_enabled())

# is_selected
male_selected = driver.find_element(By.XPATH, "//input[@id='gender-male']")
female_selected = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("Default radio button status....")
print("Male button status..", male_selected.is_selected())
print("Female button status..",female_selected.is_selected())
male_selected.click()


print("After selecting male radio button.....")
print("Male button status..", male_selected.is_selected())
print("Female button status..",female_selected.is_selected())

female_selected.click()

print("After selecting female radio button.....")
print("Male button status..", male_selected.is_selected())
print("Female button status..",female_selected.is_selected())


driver.quit()
