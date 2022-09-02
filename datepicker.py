from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# Create a webdriver object
driver = webdriver.Chrome(executable_path="/home/nikhil-95/Drivers/chromedriver")
# wait = WebDriverWait(driver, 10, ignored_exceptions=[Exception], poll_frequency=2)
# lunch browser using .get()
driver.get("https://jqueryui.com/datepicker/")
# maximize browser windows using maximize_window method
driver.maximize_window()

driver.switch_to.frame(0)

# Select month and year you want search
month = "June"
year = "2020"
date = "4"

driver.find_element(By.XPATH,"//*[@id='datepicker']").click()

ddate = False
while not ddate:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    #print(mon)
    yer = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    #print(yer)
    if mon==month and yer==year:
        ddate = True
    else:
        #driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]").click() # for next arrow we used it
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click() # for previous arrow


# Check a date and select it

dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for dat in dates:
    # print(dat.text)
    if dat.text == date:
        dat.click()
        break



