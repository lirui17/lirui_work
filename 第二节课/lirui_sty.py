# #上课第二天.  类继承 , 私有属性,私有方法,静态方法,类方法,相互调用, 异常
# #1. 类继承.子类默认继承父类的所有属性和方法.
# #(1)单继承: 一个类只继承 一个父类.父类Animal.子类Dog.
# class Thing(object):
#     def thing(self):
#         print("最大类,事务")
#
#     def eat(self):
#         print("两个父类同名的方法:子方法")
#
#
#
# class Animal(object):  # class 父类(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print("父类的吃方法,父类同名方法:父类方法")
#
#     def drink(self):
#         print("父类的喝水方法")
#
#
# class Dog(Animal):  #class 子类(父类名):
#
#     def hou_jiao(self):
#         print("子类方法吼叫")
# # #子类实例化
# # sa_mo = Dog("小黑")
# # #对象调用父类方法.  子类默认可以调用父类方法
# # sa_mo.eat()
# # #对象调用自己的方法
# # sa_mo.hou_jiao()
#
# #(2)多继承:一个类同时继承多个父类. 当一个类有多个父类的时候,默认继承第一个父类的同名属性和方法.(如两个父类都有同样名字的属性和方法,默认继承第一个)
#
#
# class JinMao(Thing, Animal):
#     pass   #当这个类或者方法中没有内容,就可以写pass
#
# #多继承类的实例化. Thing和Animal都有__init__和eat方法.本处默认继承第一个父类的__init__,和eat
# #因此需要传参. 参数和第一个类的__init__中参数一致.
# #如果其中一个类没有__init__方法,则传参和另一个类中init方法一致.如下面: 第一个父类Thing没有init. 第二个有,因此传参和第二个Animal的参数一致.
# jin_mao = JinMao("金毛")
#  #多继承子类实例化后调用方法的顺序.
# class Base(object):
#     def test(self):
#         print("爷爷类")
# class A(Base):
#     def test(self):
#         print("A重写了父类Base的test方法")
#     def test1(self):
#         pass
# class B(Base):
#     def test2(self):
#         pass
# class C(A, B):
#     pass
# #C类的实例化
# c = C()
# #对象调用方法.  查找顺序为:先找自己,再找A,后找B,最后找Base爷爷类.
# c.test()  #找自己,没有. 找A有.不会再接着找B 和Base


# #2. 子类重写父类的同名属性和方法
#
# class Animal(object):  # class 父类(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def eat(self):
#         print("父类的吃方法,父类同名方法:父类方法")
#
#     def drink(self):
#         print("父类的喝水方法")
#     def function(self):
#         #调用drink方法. 调用同一个类中的方法,要使用self.
#         self.drink()
#
# #子类Cat重写父类Animal中的eat方法
# class Cat(Animal):
#     #继承父类方法: Animal.并且重写方法:eat
#     def eat(self):
#         print("重新父类的eat方法: 子类eat猫吃")
#     def function2(self):
#         #调用本类中的方法
#         self.eat()
#         #调用另一个类(父类)的同名方法
#         super().eat()
#         #调用父类的eat方法的另一中方法
#         Animal.eat(self)
#
# # #实例化
# muchine = Cat("机器猫")
# # #子类实例化调用
# # muchine.eat()  #子类对象调用了eat方法. eat方法在子类中被重写.  所以这里调用的是子类的eat方法.  重新父类的eat方法: 子类eat猫吃
# # 子类对象调用functi2方法,就会调用 子类的eat方法和父类的eat方法
# muchine.function2()

#
# #3.多态:调用了相同的方法,但是完成的内容不同.
# # 多态首先依赖重写
# class Dog(object):
#     def hello(self):
#         print("我是普通狗.大家好")
#
#
# class Xtq(Dog):
#     def hello(self):
#         print("小弟们好,我是哮天犬")
#
#
# #且多态依赖一个外部方法,这个方法调用的 两个类中相同的这个方法
# #定义一个方法,用来调用 父类和子类中的相同方法 hello.
# def introduce(temp):
#     #本处temp表示一个对象,相当于 对象调用hello方法.
#     temp.hello()
#
# #父类实例化
# dog1 = Dog()
# #子类实例化
# dog2 = Xtq()
# #调用introduce方法.需要传参.
# introduce(dog1)  #得到的结果是 父类中的hello
# introduce(dog2)  #得到的结果是:子类中的hello

#类方法.
# (1)@classmethod 这个东西是装饰器.类方法必须在类前面加上 @classmethod .类方法和类属性是同一个级别.
# (2)括号中是 cls.表示class
# 静态方法
#私有属性.  私有属性:属于类属性  .两种写法
# 私有方法,同上
class Animal(object):
    #私有属性. 只能类内部调用.不能外部调用
    __color = "color"
    #私有属性.  类外部也能调用
    _color2 = "color2"

    #类属性
    weighe = 50
    #类方法
    @classmethod
    def fun1(cls): #类方法括号内是cls
        print("这是一个类方法")
        #在类方法中调用类属性.  cls.类属性名或者 类名.类属性名
        #一般写成 cls.类属性名.  如果写成Animal.类属性名.类的名字改变后就会报错.不利于维护
        print("在类方法中调用属性方法", cls.weighe, "或者", cls.weighe)

    #实例属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #实例方法
    def fun2(self):
        print("这是一个实例方法")
        #类内部调用类属性.  self.属性名
        return self.weighe

    #静态方法. 可以有参数,也可以没有参数.@staticmethod
    @staticmethod
    def fun3():
        print("这个是一个静态方法")
    #私有方法.不能外部调用
    def __fun4(self):
        print("这是一个私有方法")

    def use(self):
        #类内部调用实例方法  self.方法名()
        self.fun2()
        #类内部调用实例属性  self.属性名
        print("类内部的和实例属性self.name是{0}".format(self.name))
        #类内部调用类属性  类名.类属性名. 如果是 类方法中调用类属性.可以写成:  cls.类属性名
        print("类内部调用类属性self.weight是{0}".format(Animal.weighe))
        #类内部调用类方法

        #类内部调用私有属性
        print("这是一个私有属性.", self.__color)
        #类内部调用私有方法
        self.__fun4()


        #提供一个获取私有属性的方法
    def get_color(self):
        return self.__color

    #修改私有属性的值. 将参数的新值,赋值给私有属性.
    def set_color(self, color):
        self.__color = color
        return self.__color

# #类的实例化
tutu = Animal("小兔", 2)
# #类外部调用实例方法.  对象.实例方法()
# print(tutu.fun2())  #本处结果是两个
# #如果fun2中没有return.结果为: 这是一个实例方法 和None.第一个结果是:tutu.fun2()的结果.  第二个结果None是print一个函数的结果.这个函数没有返回值,所以print的结果就是none.
# #如果fun2 中有return.结果为:  这是一个实例方法he 返回值(weight=50)
#
# #类外部调用类方法.  对象.类方法()
# tutu.fun1()
#
# #类外部调用静态方法. 写法对象名.静态方法名()  或者  类名.静态方法名()
# tutu.fun3()
# Animal.fun3()
# #调用use方法

#类外部调用私有属性. 两个__,会报错. 一个_ ,可以调用
print(tutu._color2)  #假私有属性. 可以调用
#类外部调用私有方法报错.
#print(tutu.__fun4)
tutu.use()

#如果我想拿到私有属性的值
###特殊处理方法: 在类中写一个方法,这个方法访问私有属性的值. 在类外调用该方法,就能拿到 私有属性的值
#举例:在外面获取到__color的值.调用 get_color即可
print(tutu.get_color())

#如果我想修改私有属性的值.
##方法:在类中写一个方法,修改私有的值.在类外调用,把新的值传进去
#调用修改方法
print(tutu.set_color("black"))














