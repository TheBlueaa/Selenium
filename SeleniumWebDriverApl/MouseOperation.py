
# 鼠标操作——封装在ActionChains
'''
1：perform():执行ActionChains中存储的所有行为
2：context_click(): 右击
3：double_click():双击
4：drag_and_drop():拖动
5: move_to_element():鼠标悬停
'''
from selenium import webdriver
# 引入ActionChains类
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
# 定位到想要悬停的元素
above = driver.find_element_by_id("s-usersetting-top")
# 对定位到的元素进行悬停操作
# 1:点用ActionChains类，将浏览器驱动作为参数传入
ActChins = ActionChains(driver)
# 2：使用move_to_element将鼠标悬停到所选元素上，使用perform提交存储的操作
ActChins.move_to_element(above).perform()
sleep(5)
driver.close()