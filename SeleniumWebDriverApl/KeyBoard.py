
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
driver = webdriver.Chrome()
from time import  sleep
driver.get("https://www.baidu.com")

# 在输入框输入内容
driver.find_element_by_id("kw").send_keys("seleniumXXX")
sleep(3)
# 删除多打的一个XXX
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
# 删除多打的三个XXX
driver.find_element_by_id("kw").send_keys( 3 *Keys.BACK_SPACE)
sleep(3)
# 输入空格+ "教程"
driver.find_element_by_id("kw").send_keys(Keys.SPACE)
driver.find_element_by_id("kw").send_keys("教程")
# 输入组合键Ctrl + a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
sleep(3)
# 输入组合键 Ctrl + x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'X')
sleep(3)
# 输入组合键 Ctrl + c 粘贴内容到输入框
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
sleep(3)
# 用回车键代替单机操作
driver.find_element_by_id("su").send_keys(Keys.ENTER)
sleep(3)
driver.close()

