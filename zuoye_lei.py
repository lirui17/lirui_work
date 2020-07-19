# # 1.小猫爱吃鱼,小猫要喝水
# # 分析:
# #类: 猫  属性:体型shape  方法:吃鱼  喝水
#
# class Cat(object):
#     #构造函数.定义猫的属性:体型.  参数体型小,小猫
#     def __init__(self, shape):
#         self.shape = shape
#
#
#     def eat_fish(self):
#         print("{shape}猫吃鱼,然后很胖.".format(shape=self.shape))
#
#     def drink(self):
#         print("猫喝水")
#
#     def __str__(self):
#         return "这是一个类,实现了小猫吃鱼,小猫喝水"
#
# # 实例化.小猫叫花花
# flower = Cat("小")
# # 对象调用方法
# flower.drink()
# flower.eat_fish()
# # 查看类的描述
# print(flower)
#
#
# # 2.小明爱跑步,爱吃东西.  体重...
#    #小美体重....
# # 分析:对象--小明  小美,两个对象|属性:体重 | 方法:跑步  体重变化 | 类:人
# class Person(object):
#     #定义构造方法. 小明体重,小美体重不同,因此体重这个属性需要传参
#     def __init__(self, name, weight):
#         #实例属性:姓名 体重
#         self.weight = weight
#         self.name = name
#
#     #定义方法:吃东西
#     def eat(self):
#         self.weight = self.weight + 1
#         print("每次吃东西,体重加1.现在体重是{0}".format(self.weight))
#
#
#     #定义方法:跑步,然后减肥.每次调用都会减少0.5
#     def run(self):
#         self.weight = self.weight - 0.5
#         print("每次跑步体重减0.5,现在体重是{0}".format(self.weight))
#
# #小明的打印内容
# #实例化
# xiaoming = Person("小明", 75.0)
# #调用eat方法
# xiaoming.eat()
# #调用run方法
# xiaoming.run()

#小美的打印内容
xiaomei = Person("小美", 45.0)
#类外部的调用类中的属性
print("小美的体重是{0}".format(xiaomei.weight))

# #摆放家具
# #类:home   属性:家具(furn)  户型(layout)   房子面积:house_aera   家具面积:furn_area  剩余面积:left_area
# #方法: 放家具
#
# class Home(object):
#
#     #构造方法,包含属性,并且新房子剩余面积是房子面积
#     def __init__(self, layout, house_area, *furn):
#         #实例属性. 户型  房屋面积   剩余面积  家具
#         self.layout = layout
#         self.house_area = house_area
#         self.left_area = house_area
#         #最后房间内的家具要生成列表.因此初始化家具作为一个空列表
#         self.furn = []
#
#     #定义方法:计算家具和
#     def sum_furn(self, furn_name):
#         # 计算家具面积和
#         if furn_name == ("床", "餐桌", "衣柜"):
#             return 7.5
#
#     #方法:放家具,计算剩余面积
#     def add_furn(self, *furn_name):
#         #将新放进的家具添加至列表中
#         self.furn.append(furn_name)
#    #     sum1 = self.sum_furn(furn_name)
#         self.left_area = self.house_area - Home.sum_furn(self, furn_name)
#
#     def __str__(self):
#         return "该房子的户型是%s,总面积是%5.1f,剩余面积是%5.1f,其中家具有%s" % (self.layout, self.house_area, self.left_area, self.furn)
#
# #打印结果
# my_house = Home("三居室", 100.0, "床", "衣柜", "餐桌")
#
# my_house.add_furn("床", "餐桌", "衣柜")
# #打印结果
# print(my_house)  #该房子的户型是三居室,总面积是100.0,剩余面积是 92.5,其中家具有[('床', '餐桌', '衣柜')]
#


# # 类和方法 :士兵(扣动扳机) + 枪 (发射 装弹)
# #对象:rain   AK47
# #属性 :sold_name   gun_name
#
#
# class Soldiers(object):
#     #类属性
#     gun_name = "AK47"
#     #定义构造函数
#     def __init__(self, sold_name):
#         #实例属性: 人名
#         self.sold_name = sold_name
#
#
#     #定义方法:扣动扳机
#     def shut(self):
#         print("{0}扣动了扳机".format(self.sold_name))
#
#     #一个类不能访问另一个类中的实例属性.因此把 枪名属性写到了 类属性里面.
#     def __str__(self):
#         return "{0}有一把{1}".format(self.sold_name, self.gun_name)
#
#
# class Gun(object):
#     def __init__(self, gun_name):
#         # 构造函数,实例属性枪名
#         self.gun_name = gun_name
#
#     #定义方法:发射子弹
#     def go(self):
#         print("%s发射了子弹" % self.gun_name)
#
#     #定义方法:增加子弹
#     def add_go(self):
#         print("%s装了子弹" % self.gun_name)
#
# #打印士兵相关
# rain = Soldiers("rain")
# print(rain)
# #对象调用开火
# rain.shut()
#
#
#
#






















