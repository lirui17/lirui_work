# #类: 描述有相同的属性(特征,变量)和方法(函数)的对象的集合.
# #1.关于类变量的种类: 类外部变量 +类内部变量(类变量+实例变量)
# #2.创建类:  class 类名(object). 类名要满足大驼峰.所有单词首字母大写.
# #3. 在书写时,类中:只能有两部分. 类变量以及方法.   不能有其他部分的代码.如果需要实现什么.需要写在方法中.
#
# class Dog(object):
#     #类变量.
#     typee = "pet"
#
#     #这是一个构造函数(初始化方法). self必须写.self也是一个参数. 其他参数可有可无.
        #初始化属性.给属性一个初始值. 如果给属性初始值,意味着所有的对象都是这个初始值. 在使用时,就被写死.
# 因此可以在__init__函数中传入参数,跟随每一个对象.这样就对象和对象之间这个参数就可以不一样.

#     def __init__(self, name, age, color):
#         #实例属性. (实例变量)实例属性必须写在__init__构造函数中.
#         #实例属性书写方式,必须是 self.xx
#         #name表示形参,外部传递实参时形参接收,
#         #self.name中的name是:定义的变量
#         self.name = name
#         self.age = age
#         self.color =color
#
#
#     #普通方法.
#     def eat(self):
#         print("狗仔吃东西")
#     #普通方法也路传递参数.因此在对象调用方法时,也需要传参
#     def run(self, speed):
#         #本处的名字需要用到的是变量名. 在实例属性中,name形参赋值给变量self.name.因此这里用self.name
#         #self参数表示当前对象. 因此self.name = taidi.name
#         print(self.name, "的第二个方法:跑,速度为", speed)
#
#     #__str__函数定义后,print(对象)可以得到return的内容.
#     #return内容一般写当前类的介绍
#     def __str__(self):
#         return "这是一个类.其中包含eat和run方法"
#     #当删除对象时,对象会自动默认调用__del__方法.
#     def __del__(self):
#         print("对象被删除了")
#
# #类的实例化.  就是把类赋值给一个对象. 狗是一个类,包含很多个具体的实例.对象名 = 类名()
#
# #__init__函数:在对象实例化时,会自动调用init函数. 由于init函数中有参数,在实例化时也需要传参.
# #init函数中一共有4个函数.  本处只能传递3个. self为隐式传递,代表对象. 因此只需要传递除self以外的参数.
# taidi = Dog("花花", 2, "black")
#
#
# #对象调用类中的方法.   对象.方法名()
# taidi.eat()  #狗仔吃东西.其实传递了一个参数self
#
# #在类的外部,为对象添加新属性,  对象名.新属性名 = "新属性"
# taidi.hair = "long"
# print(taidi.hair)
# #在类外部,修改对象的属性.  对象名.原属性名 = 新值
# taidi.color = "red"
# print(taidi.color)  #red
#
# #对象调用run方法传参speed
# taidi.run(3)
#
#
# #self关键字解释
# #1.对象实例化时,会自动调用init方法.因此必须传递 init中相同数量的参数
# #2.self表示当前对象.  默认会传递.因此对象实例化和对象调用方法时,self不需要写.
# #3. name表示形参,外部传递实参时形参接收.self.name中的name是:定义的变量
#
#
# # 当类中没有定义 __init__,直接print对象时,得到对象的内存地址.
# print(taidi)  #<__main__.Dog object at 0x00E01FE8>
# #当类中定义了__init__方法时,print(对象)可以得到 __init__方法中return的内容
# #因此,__init__方法中return内容一般是:当前类的介绍.
# print(taidi)  #这是一个类.其中包含eat和run方法
#
#
# #删除对象.  del 对象名
# del taidi
#

# 烤地瓜. 地瓜状态:生 半生不熟  熟 糊  .  调料:加 不加---方法
# 属性: 烤地瓜的时间 地瓜状态  添加的调料
# 方法: 烤地瓜,判断     加调料
# 分析:1.烤地瓜方法中需要传入时间. 时间作为一个属性.因此烤地瓜方法需要一个参数 time
# 2.加入调料也作为一个属性,需要传递.

# #定义一个类.地瓜
# class Potato(object):
#     #定义构造函数.初始化属性.  时间0,状态生的,不加调料
#     def __init__(self):
#         self.status = "生的"
#         self.time = 0
#         self.cooper = "不加"
#
#     #定义cook烤地瓜方法.
#     def cook(self, time):
#         #
#         self.time = self.time + time
#         if 0 <= self.time < 3:
#             self.status = "生的"
#         elif 3 <= self.time < 5:
#             self.status = "半生不熟"
#         elif 5 <= self.time < 8:
#             self.status = "熟的"
#         else:
#             self.status = "烤糊了"
#
#     def coop(self, cooper):
#         #定义加调料方法. 参数 调料
#         self.cooper = cooper
#
#     def __str__(self):
#         #定义类的解释
#         return "这个地瓜考了{0}分钟,状态是{1},{2}调料".format(self.time, self.status, self.cooper)
#
# #类的实例化. 地瓜叫wq
# wq = Potato()
# #对象调用cook方法,需要传参
# wq.cook(6)
# #调用调料方法
# wq.coop("番茄")
# #查看类的描述. 直接打印对象
# print(wq)



# 方法:烤地瓜.
#
# # 该方法mo,中不涉及对属性的操作. 因此方法名下方有下划线,提示method mo may be static.
# # 报错描述:在类中定义方法时,若该方法不涉及对属性的操作,就会报错
# # 解决办法: 删除方法中的self. 然后申明一下静态变量
# @staticmethod
# def mo(self, cook_add):
#     "添加调料"
#     print("添加的调料是:", cook_add)
#

#方法二:  time参数,和调料参数由用户输入. 定义一个input方法

#
# class Potato(object):
#     #我觉得__init__函数不需要写.
#     #定义init属性
#     # def __init__(self):
#     #     self.status = "生的"
#     #     self.time = 0
#     #     self.cooper = "不加"
#
#     #定义一个input方法,让用户输入time和coop
#     def user_input(self):
#         self.time = int(input("请输入烤地瓜的时间"))
#         self.cooper = input("请输入口味")
#         self.status = "生的"
#
#     #定义一个烤地瓜方法.并且判断地瓜状态
#     def cook(self):
#
#         if 0 <= self.time < 3:
#             self.status = "生的"
#         elif 3 <= self.time < 5:
#             self.status = "半生不熟"
#         elif 5 <= self.time < 8:
#             self.status = "熟的"
#         else:
#             self.status = "烤糊了"
#
#     def coop(self):
#         "加入调料"
#         print("加入了调料", self.coop)
#
#     def __str__(self):
#         #定义类的解释
#         return "这个地瓜考了{0}分钟,状态是{1},{2}调料".format(self.time, self.status, self.cooper)
#
# #实例化
# LR = Potato()
#
# #调用input
# LR.user_input()
#
# #调用考地瓜方法
# LR.cook()
# #查看类的描述.打印对象
# print(LR)




#家具需求: 将小于房⼦子剩余⾯面积的家具摆放到房子中
# 分析: 类题目中两类实物是家具和房子. 家具:furn
# 类: 面积
# 属性:  家具面积  房子面积   剩余面积
#方法 : 计算面积   放进去

#定义类: 面积
class Area(object):
    #定义构造函数,定义实例属性.
    #创建对象时参数为: 家具面积,房子面积,家具名字
    def __init__(self, furn_area, house_area, *furn_name):
        #furn_area和house_area为形参. 带self的是本方法中形参赋予的属性名
        self.furn_area = furn_area
        self.house_area = house_area
        self.left_area = self.house_area - self.furn_area
        self.furn_name = furn_name
        self.furn_adds = []
    #定义方法:加入家具

    def add_furn(self):
        if self.furn_area <= self.left_area:
            print("{0}家具面积小于房子剩余面积{1},可以加入".format(self.furn_name, self.left_area))
            #如果加入家具,则放入家具列表
            self.furn_adds.append(self.furn_name)
        else:
            print("{0}家具的面积大于房子面积,放不进去".format(self.furn_name))
     #定义str描述

    def __str__(self):
        return "房子面积是{0},家具面积是{1},剩余面积是{2},房间已经有家具是{3}".format(
            self.house_area, self.furn_area, self.left_area, self.furn_adds)


#实例化
lr = Area(4, 100, "床", "桌子")
lr.add_furn()
print(lr)










