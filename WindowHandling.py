import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://phptravels.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.delete_all_cookies()

current_window_id = driver.current_window_handle
print(current_window_id)
time.sleep(10)
driver.find_element_by_xpath("//span[text()='Login']").click()
window_ids = driver.window_handles
type(window_ids)
print(window_ids)
for handle in window_ids:
    print(handle)
    if handle != current_window_id:
        driver.switch_to.window(handle)
        driver.find_element_by_name("username").send_keys("test")

driver.quit()
