import time

from selenium import webdriver


driver = webdriver.Chrome(r"C:\Users\22016\Martin\software\chrome-win64\chrome.exe")  # Optional argument, if not specified will search path.
print(driver)
driver.get(r"http://www.google.com/")
time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!

driver.quit()