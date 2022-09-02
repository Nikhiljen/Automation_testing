from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# Create a webdriver object
driver = webdriver.Chrome(executable_path="/home/nikhil-95/Drivers/chromedriver")
# wait = WebDriverWait(driver, 10, ignored_exceptions=[Exception], poll_frequency=2)
# lunch browser using .get()
driver.get("https://demo.automationtesting.in/Frames.html")

# maximize browser windows using maximize_window method
driver.maximize_window()

driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()

# If there is name or id of frame is not availbale then get webelement of it then switch into that frame

outerframe = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Welcome")

# if you want to return parent frame from child frame then used this command
#driver.switch_to.parent_frame()

# if you want to return to brower main page
driver.switch_to.default_content()
print(driver.title)