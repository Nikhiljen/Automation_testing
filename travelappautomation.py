import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Create a webdriver object
driver = webdriver.Chrome(executable_path="/home/nikhil-95/Drivers/chromedriver")
# lunch browser using .get()
driver.get("https://www.dummyticket.com/")
# maximize browser windows using maximize_window method
driver.maximize_window()

# Select your currency where you want to transaction do it
Currency = "INR"
currency = driver.find_elements(By.XPATH,"/html/body/div[3]/div/a")
for cu in currency:
    # print(cu.text)
    if cu.text == Currency:
        cu.click()
        break

# click on buy ticket options
driver.find_element(By.LINK_TEXT,"Buy Ticket").click()

# product selection

#package = "Dummy ticket for Visa Application"
clicked = driver.find_element(By.XPATH,'//*[@id="product_550"]')
isclick = clicked.is_selected()
print(isclick)
if isclick is True:
    clicked.click()

# Insert first and last name
firstName = "Nikhil"
lastName = "Jengte"
driver.find_element(By.XPATH,"//*[@id='travname']").send_keys(firstName)
driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys(lastName)

# Birthday of traveller
Month = "Jun"
Year = "1992"
Date = "4"

driver.find_element(By.ID,'dob').click()
ddate = False
year = driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']")
yeardp = Select(year)
yeardp.select_by_visible_text(Year)

month = driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']")
monthdp = Select(month)
monthdp.select_by_visible_text(Month)

date = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for dd in date:
    if dd.text == Date:
        dd.click()
        break

total = driver.find_elements(By.XPATH,"//*[@id='sex_field']/span/input")
print(len(total))
for i in range(len(total)):
    total[i].click()


otherperson = driver.find_element(By.XPATH,"//*[@id='addmorepax']")
print(otherperson.text)
for i in range(2):
    print("Other person status is", otherperson.is_selected())
    if not otherperson.is_selected():
        otherperson.click()
        break
    else:
        otherperson.click()