
# 导入selenium的webdrive模块
from selenium import webdriver
from time import sleep
# 调用webdrive模块下面的Chrome()类 ！！！（注意大小写），赋值给变量driver
drive = webdriver.Chrome()
# 通过drive变量，调用Chrome()类提供的方法 get()方法去访问百度的主页
drive.get("https://www.baidu.com/")
# 通过find_element_by_id()方法定位元素通过send_keys，click做输入，点击操作
drive.find_element_by_id("kw").send_keys("Selenium")
drive.find_element_by_id("su").click()
sleep(5)
# 关闭浏览器
drive.quit()
