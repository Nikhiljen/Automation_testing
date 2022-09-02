import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a webdriver object
driver = webdriver.Chrome(executable_path="/home/nikhil-95/Drivers/chromedriver")
wait = WebDriverWait(driver, 10, ignored_exceptions=[Exception], poll_frequency=2)
# lunch browser using .get()
driver.get("http://www.deadlinkcity.com/")

# maximize browser windows using maximize_window method
driver.maximize_window()

# brokenlink = driver.find_elements(By.TAG_NAME,'a')

Totallink = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
print("Total links available on this page is", len(Totallink))
total_broken_link_count = 0
total_valid_link_count = 0
for link in Totallink:
    url = link.get_attribute("href")
    try:
        responce = requests.head(url)
    except:
        None

    if responce.status_code >= 400:
        print(url, "is broken link")
        total_broken_link_count += 1
    else:
        print(url, "is valid links")
        total_valid_link_count += 1
print("Total Valid link ", total_valid_link_count)
print("Total broken link ", total_broken_link_count)

driver.quit()
