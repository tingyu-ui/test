# try:
#     num1 = int(input("输入一个除数"))
#     num2 = int(input("输入一个被除数"))
#     print(num1/num2)
# except ZeroDivisionError:
#     # print("这是一个异常")
#     print("被除数不能为0")
# except:
#     print("请输入数值型整数")

# except:
#     print("这是一个能用型异常")
# else:
#     print("程序没有发生异常")
# finally:
#     print("无论发没发生异常，都执行")
# x = 10
# if x>5:
#     raise Exception("这是抛出的异常信息")

class MyException(Exception):
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2
raise MyException("value1","value2")