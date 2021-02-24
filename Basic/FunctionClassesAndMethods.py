'''
# 定义函数_function
def add (a,b):
    print(a+b)
add("YZM","加油")
add(2,3)

def add2(d,e):
    return ( d + e )
c = add2(3,5)
print(c)

def add3(a = 1,b = 2):
    return (a + b)
c1 = add3()
c2 = add3(3,5)
print(c1)
print(c2)
'''

# 定义一个MyClass类
class MyClass(object):
    def say_hello(self,name):
        return "hello," +name
# 调用MyClass类
# mc = MyClass()
#
# print(mc.say_hello("tom"))
# print(MyClass().say_hello("李娇"))

# class A:
#     def __init__(self, a, b):
#         self.a = int(a)
#         self.b = int(b)
#     def add(self):
#         return self.a + self.b
# # 调用类的时候需要传入初始化参数
# cout = A(2,'4')
# print(cout.add())
# class B(A):
#     def sub(self, a, b):
#         return a - b
# print(B(100,1).sub(10,1))
#
