'''
#调用 time 模块
import  time
#  time() 下面ctime()函数用于当前时间
print(time.ctime())
'''
'''
# 仅仅调用 ctime() 函数
from  time import ctime
print(ctime())
'''
'''
# 直接导入多个函数
from time import time,sleep
'''
'''
from  time import *
print(ctime())
print("休眠 5 s")
sleep(5)
print(ctime())
'''
'''
from time import sleep as sys_sleep

def sleep():
    sys_sleep(3)
    print("三秒后打印")
    print("this is I defined sleep() ")
sleep()

help(sys_sleep())
'''
'''
# 查看time模块
import time
help(time)
'''
'''
import sys
from FunctionClassesAndMethods import MyClass
print(MyClass().say_hello("这是模块的调用"))
for i in sys.path:
    print(i)
'''

'''
# 掉用其他模块 绝对路径
import sys
from os.path import dirname,abspath
project_path = abspath(".")
print(project_path)
sys.path.append("//Users//TheBlueaa//Selenium")
from Auto.Day01_01 import sleep
sleep()
'''


