import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# import time

# Create a webdriver object
driver = webdriver.Chrome(executable_path="/home/nikhil-95/Drivers/chromedriver")

# lunch browser using .get()
driver.get("https://www.opencart.com/index.php?route=account/register")

# maximize browser windows using maximize_window method
driver.maximize_window()

dropdown = driver.find_element(By.XPATH, "//select[@id='input-country']")
drpcountry = Select(dropdown)

# drpcountry.select_by_visible_text("India")
# drpcountry.select_by_value('10')
# drpcountry.select_by_index(13)

# Capture all options and select them

alloptions = drpcountry.options

print("Toal options are available", len(alloptions))

# select one options without using build in method

for opt in alloptions:
    if opt.text == "India":
        opt.click()
        break

time.sleep(2)
driver.quit()
