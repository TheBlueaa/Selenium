from time import  sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://email.163.com/#module=welcome.WelcomeModule%7C%7B%7D")
sleep(2)

login_frame = driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
driver.switch_to.frame(login_frame)
driver.find_element_by_name("email").send_keys("18384549714@163.com")
driver.find_element_by_name("password").send_keys("981014Yzm.")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()
sleep(3)
driver.close()