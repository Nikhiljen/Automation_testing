from selenium import webdriver
from selenium.webdriver.common.by import By
# import time

# Create a webdriver object
driver = webdriver.Chrome(executable_path="/home/nikhil-95/Drivers/chromedriver")

# lunch browser using .get()
driver.get("https://demo.nopcommerce.com/")

# maximize browser windows using maximize_window method
driver.maximize_window()

# click on links
# link = driver.find_element(By.LINK_TEXT,'Digital  downloads').click()
# links_partial = driver.find_element(By.PARTIAL_LINK_TEXT,'Apple MacBook Pro').click()
# Used Link_text mostly Partial_link_test is not recommended

# find a total number of links available in this page
# total_links = driver.find_elements(By.TAG_NAME, 'a')
# print(len(total_links))

# Find total Number of links using XPATH
total_links = driver.find_elements(By.XPATH, '//a')
print("Total Number of links: ", len(total_links))

# Print all links text
links_list = list()

for i in total_links:
    links_list.append(i.text)

print(links_list)
