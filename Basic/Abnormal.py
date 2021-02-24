'''
try:
    open("abc.txt","r")
except FileNotFoundError:
    print("这是没有找到文件的异常")

# try:
#     print(a)
# except FileNotFoundError:
#     print("这是异常用错了")

try:
    print(a)
except NameError:
    print("没有找到变量")

try:
    open("abc.txt",'r')
except BaseException:
    print("这个能接受所有的异常")

try:
    open("abc.txt",'r')
except BaseException as  msg:
    print(msg)
'''
'''
常用的异常
BaseException：新的所有的异常的基类—
Exception：所有异常的基类，但继承自BaseException的类
AssertionError: assert语句失败
AttributeError：试图访问的对象没有属性
FileNotFoundError：试图打开一个不存在的文件或者目录
OSError：当系统函数返回一个系统相关的错误（包括I/o故障），如："找不到文件"or"磁盘已满"时，引发此异常
NameError：使用一个还未赋值的变量
IndexError：当一个序列超出范围的异常
SyntaxError：当解析器遇到一个语法错误时，引发此异常
KeyboardInterrupt：组合键 ctel +  c 程序被强行终止
TypeError：传入的对象类型与要求不符合
'''
#
# try:
#     a = "Abonrmmal test"
#     print(a)
# except BaseException as msg1:
#     print(msg1)
# else:
#     print("没有异常的时候执行")
#
# try:
#     print(b)
# except NameError as msg2:
#     print(msg2)
# finally:
#     print("最后都会执行这个")

#定义哥say_hello（）函数
def Say_hello(name = None):
    if name is None:
        raise NameError('"name"cannot be empty')
    else:
        print("hello,%s" %name)
Say_hello()
