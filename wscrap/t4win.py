import time
from selenium import webdriver

url = "https://google.com/"
driver = webdriver.Chrome()
print(driver)
driver.get(r"http://www.google.com/")
time.sleep(5) # Let the user actually see something!



# search_box = driver.find_element_by_name('q')
search_box = driver.find_element('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!

driver.quit()
