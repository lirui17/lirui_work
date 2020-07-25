#
# #异常.异常就是报错,看最后一行的提示信息.
# #1.用处:出错后,让代码继续执行.
#
# #1.捕获异常
# #(1)如果有try语句有异常,就执行 except后面的语句
# #以r只读方式打开text.txt. 如果报错了,就 以写w的方式打开这个文件.
# #r:如果文件不存在,就报错.  w: 如果文件不存在,就建一个
# try:
#     open("text.txt", "r")
# except:
#     open("text.txt", "w")
#
# #(2)捕获指定异常.  如果这个错误是xxx, 就执行except后面的语句
# #如果try后面的代码报的错,和捕获的类型(except后面的词)不一致,则无法捕获异常
# # 一般except后面只放一行代码
# try:
#     print(number)
# except NameError:
#     print("这个变量没有定义")
#
# #(3)捕获多个指定异常.  查询方式:先查看是否报的是第一个NameError.如果不是,查看第二个.
# #如果第一个就匹配,就会执行except后面的语句.
# try:
#     print(1/0)
# except (NameError, ZeroDivisionError):
#     print("有错误")
#
# #(4)捕获异常的描述信息. 这种格式可以得到错误的详细描述信息.
# try:
#     print(1/0)
# except (NameError, ZeroDivisionError) as result:
#     print(result)
#
# #(5)捕获所有异常.这里的Exception是一个类. 以上所有的报错信息,都是一个类. 这些类都继承了  Excrption这个类.
# #因此直接写 基类Exception,可以捕获所有异常
# #下面有两个错误:0不能作为除数.   num没有定义.但是只能得到一个错误的描述信息,因此有一个错,就不会继续执行
# try:
#     print(1/0, num)
# except Exception as result:
#     print(result)
# #(6)else . else后面:如果没有异常则执行else后面的代码
# #下面执行完成的结果是:   0.1666666666666和没有异常.
# #因为:没有异常,所以不执行except的内容
# try:
#     print(1/6)
# except (NameError, ZeroDivisionError) as result:
#     print(result)
# else:
#     print("没有异常")

#(7)finally: 无论有没有异常,都会执行
try:
    print(1/0)
except (NameError, ZeroDivisionError) as result:
    print(result)
else:
    print("没有异常")
finally:
    print("这句话无论有没有异常,都会执行")


























































