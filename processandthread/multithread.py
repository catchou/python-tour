import time, threading

# 新线程执行的代码
def loop():
    print('thread %s is running' % threading.current_thread().getName())
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s print %s' %(threading.current_thread().getName(), n))
        time.sleep(1)
    print('thread %s end.' % threading.current_thread().getName())

print('thread %s is running' % threading.current_thread().getName())
time.sleep(3)
t = threading.Thread(target=loop, name='Loop Thread')
t.start()
t.join()
print('thread %s end.' % threading.current_thread().getName())