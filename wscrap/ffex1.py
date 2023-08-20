from selenium import webdriver
from selenium.webdriver.common.keys import Keys

profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', '/tmp')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')


driver = webdriver.Firefox(profile)
driver.get("http://www.diva-gis.org/gdata")
driver.find_element_by_name('OK').click()
driver.find_element_by_css_selector("#node-39 > div > div > div > div > a > h2").click()
