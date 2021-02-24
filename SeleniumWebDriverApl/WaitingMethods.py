
from selenium import webdriver
from time import sleep,ctime
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import NoSuchFrameException

# 显式等待
'''
driver = webdriver.Chrome()
driver.get("http://ww.baidu.com")
print(ctime())
for i in  range(10):
    try:
        element = driver.find_element_by_id("kw22")
        if element.is_displayed():
            break
    except:
        pass
    sleep(1)
else:
    print("time out")
print(ctime())
driver.quit()
driver.close()

'''
# element = WebDriverWait(driver,0.1,0.5).until(
#     EC.visibility_of_element_located((By.ID,"kw"))
# )
# element.send_keys('selenium')
# sleep(1)
# driver.close()

'''
# title_is  判断当前页面的标题是否等于预期
# WebDriverWait(driver,5,0.5).until_not(
#     EC.title_is("百一下，你就知道")
# )
# title_contains  判断当前页面是否包含预期字符串
# WebDriverWait(driver,3,0.2).until(
#     EC.title_contains("百度")
# )
# sleep(1)
# driver.close()
'''
#隐式等待
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://ww.baidu.com")
try:
    print(ctime())
    driver.find_element_by_id("kw22").send_keys("seleium")
except NoSuchFrameException as  e:
    print(e)
finally:
    print(ctime())
    driver.close()
