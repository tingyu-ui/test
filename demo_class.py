#通过class关键字，定义了一个类
#创建一个人类
class Person:
    #类变量
    name = "default"
    age = 0
    gender = 'male'
    weight = 0
#构造方法，在类实例化的时候被调用
    def __init__(self,name,age,gender,weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        # print("init function")

    # def set_param(self,name,age,gender,weight):
    #     self.name = name
    #     self.age = age
    #     self.gender = gender
    #     self.weight = weight

    # def set_age(self,age):
    #     self.age = age
    #装饰器
    @classmethod
    def eat(self):
        print(f"{self.name} eating")
        print("xxxx")
        # print("eating")

    def play(self):
        print("playing")

    def jump(self):
        print("jump")

#类方法是不能访问实例方法
#前面加了@classmethod才可以
Person.eat()
# zs = Person ('zhangsan',20,'男',120)
# zs.eat()

#类变量和实例变量区别
#类变量是需要类来访问的，实例变量是需要实例来访问
# print(Person.name)
# Person.name = 'tom'
# print(Person.name)
#
# zs = Person('zhangsan',20,'男',120)
# print(zs.name)
# zs.name = 'lili'

#类的实例化，创建了一个实例
# zs = Person()
# print(zs.name)
# zs = Person('zhangsan',20,'男',120)
# zs.eat()
# zs.set_param('zhangsan')
# zs.set_age(20)
# print(f"zhangsan 的姓名是：{zs.name},zhangsan的年龄是：{zs.age}")
# print(f"zhangsan 的性别是：{zs.gender},zhangsan的体重是：{zs.weight}")

#
# ls = Person('lisi',30,'男',150)
# # zs.set_param('zhangsan')
# # zs.set_age(20)
# ls.jump()
# print(f" 李四的姓名是：{ls.name},李四的年龄是：{ls.age}")
# print(f"李四 的性别是：{ls.gender},李四的体重是：{ls.weight}")