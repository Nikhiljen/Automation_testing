from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# Create a webdriver object
driver = webdriver.Chrome(executable_path="/home/nikhil-95/Drivers/chromedriver")
# wait = WebDriverWait(driver, 10, ignored_exceptions=[Exception], poll_frequency=2)
# lunch browser using .get()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# maximize browser windows using maximize_window method
driver.maximize_window()

Month = "Jun"
Year = "1992"
Date = "4"

driver.find_element(By.ID,'dob').click()

ddate = False

# for years, we have to apply different logic

year = driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']")
drpyear = Select(year)
alloptions = drpyear.options
for opt in alloptions:
    if opt.text == Year:
        opt.click()
        break


# select month using dropdown

month = driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']")
drpmonth = Select(month)
alloptions = drpmonth.options
for opt in alloptions:
    #print(opt.text)
    if opt.text == Month:
        opt.click()
        break

date = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in date:
    if ele.text == Date:
        ele.click()
        break


