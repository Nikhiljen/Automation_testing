from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# Create a webdriver object
driver = webdriver.Chrome(executable_path="/home/nikhil-95/Drivers/chromedriver")
# wait = WebDriverWait(driver, 10, ignored_exceptions=[Exception], poll_frequency=2)
# lunch browser using .get()
driver.get("https://opensource-demo.orangehrmlive.com")

# maximize browser windows using maximize_window method
driver.maximize_window()

# driver.current_window_handle
# print(driver.title)

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a').click()

# Get multiple window id
winid = driver.window_handles

for id in winid:
    driver.switch_to.window(id)
    print(driver.title)

# to close specific window
for id in winid:
    driver.switch_to.window(id)
    if driver.title == "OrangeHRM":
        driver.close()