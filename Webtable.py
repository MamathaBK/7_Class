from selenium import webdriver

driver = webdriver.Chrome()
driver.get("C:/Users/Mamatha/Desktop/webtable.html")
driver.maximize_window()
driver.implicitly_wait(20)

elements = driver.find_elements_by_xpath("//*[@id='emp']/thead/tr/th")
print(type(elements))
print(len(elements))

first_elements = driver.find_elements_by_xpath("//*[@id='emp']/tbody/tr[1]/td")
print(type(first_elements))
print(len(first_elements))

total_rows = driver.find_elements_by_xpath("//*[@id='emp']/tbody/tr")
print(type(total_rows))
print(len(total_rows))
