
from selenium import webdriver
driver = webdriver.Chrome()
from time import  sleep


driver.get("https://www.baidu.com")
# driver.find_element_by_id("kw").send_keys("senlenium")
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("test")
# driver.find_element_by_id("su").click()
# driver.close()
# 获取输入框的尺寸
size = driver.find_element_by_id("kw").size
print(size)
# 返回百度页面的底部备案信息
text = driver.find_element_by_id("bottom_layer").text
print(text)
# 返回元素的属性 可以是id，name,type或者其他任意属性
attribute = driver.find_element_by_id("kw").get_attribute("name")
attribute2 = driver.find_element_by_id("kw").get_attribute("id")
attribute3 = driver.find_element_by_id("kw").get_attribute("type")
print(attribute)
print(attribute2)
print(attribute3)
# 返回元素的结果是否可见，返回结果是否为True 或者False
result = driver.find_element_by_id("kw").is_displayed()
print(result)
driver.close()