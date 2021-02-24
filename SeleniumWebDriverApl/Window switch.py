import time
from selenium import webdriver

# current_window_handle：获取当前窗口的句柄
# window_handles：返回所有窗口的句柄到当前会话
# switch_to.window（）： 切换到相应的窗口
driver = webdriver.Chrome()
driver.maximize_window()
# 隐式等待，10秒
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
# 获取百度搜索窗口句柄
search_windows = driver.current_window_handle
driver.find_element_by_xpath('//*[@id="u1"]/a').click()
driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()

# 获取当前所有打开的窗口的句柄
all_handles = driver.window_handles
# 进入注册窗口
for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print(driver.title)
        driver.find_element_by_name("userName").send_keys("username")
        driver.find_element_by_name("phone").send_keys("18384549714")
        time.sleep(3)
        #~
        # 关闭当前窗口
        driver.close()
# 回到搜索窗口
time.sleep(5)
driver.switch_to.window(search_windows)
print(driver.title)
driver.quit()