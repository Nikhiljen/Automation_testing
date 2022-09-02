from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a webdriver object
driver = webdriver.Chrome(executable_path="/home/nikhil-95/Drivers/chromedriver")

# lunch browser using .get()
driver.get("https://itera-qa.azurewebsites.net/home/automation")

# maximize browser windows using maximize_window method
driver.maximize_window()

# Select a single checkbox
# driver.find_element(By.XPATH,"//input[@id='monday']").click()

# select multiple check boxes at one time
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox'  and contains(@id,'day')]")
print(len(checkboxes))

# check all checkbox correctly
# Approach 1
'''for i in range(len(checkboxes)):
    checkboxes[i].click()'''

# Approach 2
for checkbox in checkboxes:
    checkbox.click()
time.sleep(2)
# Approach 3
# select specific checkboxes
'''for checkbox in checkboxes:
    week-name = checkbox.get_attribute('id')
    if week-name == "monday" or week-name == "sunday" or week-name == "wednesday" :
        checkbox.click()'''

# Approach 4
# select last 2 day
'''for i in range(len(checkboxes)-2,len(checkboxes)):
    checkboxes[i].click()'''

# Approach 5
# Select first 2 day
'''for i in range(len(checkboxes)):
    if i < 2:
        checkboxes[i].click()'''
# Approach 6
# Clear all selected
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()


time.sleep(2)
driver.quit()
