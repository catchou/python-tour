import time

# 装饰器

# 这个装饰器支持可变参数和关键字参数
def decorator(func):
    # *args无法支持f3的关键字参数，需要加上**kw参数
    def wrapper(*args, **kw):
        print('time:%s' % time.time())
        func(*args, **kw)
    return wrapper

# 此处@decorator的作用等同于：
# decorator(f1)
#
@decorator
def f1(func_name):
    print('This is function named %s' % func_name)

@decorator
def f2(func_name1, func_name2):
    print('This is function named %s' % func_name1)
    print('This is function named %s' % func_name2)

@decorator
def f3(func_name1, func_name2, **kw):
    print('This is function named %s' % func_name1)
    print('This is function named %s' % func_name2)
    print(kw)

#f1('test func')
#f2('func1', 'func2')

f3('fname1','fname2', a=1, b=True, c = 'hello world^^')
