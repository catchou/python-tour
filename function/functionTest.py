# 函数式编程和闭包
def a():
    pass

#print(type(a))

# 抛物线函数
def curve_pre():
    a = 10
    def curve(x):
        return a*x*x
    return curve

f = curve_pre()
#print(type(f))
a = 1
# f的type是function
#print(f(2))
#print(f.__closure__[0].cell_contents)

# 闭包 = 函数+环境变量(函数外部的环境变量，但不是全局变量)
#
def f1():
    a = 10
    def f2():
        #a = 1
        c = 1 + a
        #print(a)
        return c
    #print(a)
    return f2

    #print(a)
# f2不是闭包
# f2中对a进行了赋值，python认为a是局部变量而不是f2外部的变量
# 在f2中引用a时，f2可认为闭包；而在f2中对a进行赋值时，f2不是闭包
f = f1()
print(type(f))
print(f.__closure__)

