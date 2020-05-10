from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/')
sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
with open('page.html', 'w') as f:
    f.write(driver.page_source)

print(0)