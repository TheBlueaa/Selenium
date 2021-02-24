
from selenium import webdriver
driver = webdriver.Chrome()
from time import  sleep
'''
driver.get("https://www.baidu.com/")
# # 设定参数数字为像素
# print("设置浏览器宽：480，高800显示")
# driver.set_window_size("480,800")
# driver.quit()
# print("设置浏览器全屏显示")
driver.maximize_window()
sleep(5)
driver.close()
'''

'''
#控制浏览器
# 访问百度首页
first_url = "https://www.baidu.com/"
print("now access %s" %(first_url))
driver.get(first_url)
# 访问新闻页
second_url = "http://news.baidu.com/"
print("now access %s" %(second_url))
driver.get(second_url)
# 后退/返回到首页页
sleep(2)
print("back to %s" %(first_url))
driver.back()
#前进到新闻页
sleep(3)
print("forword to %s" %(second_url))
sleep(2)
driver.refresh()
print("现在正在刷新")
driver.forward()
sleep(3)
driver.close()
 '''
# webdirver的常用方法
# 1: clear(): 清除文本
# 2：send_keys(value) ： 模拟输入
# 3: click(): 点击元素
# 4: submit(): 提交表单
# 5: size : 返回元素的尺寸
# 6: test : 获取元素的文本
# 7: get_attribute(name) : 获得属性值
# 7: is_diplayed() : 设置该元素是否用户可见

