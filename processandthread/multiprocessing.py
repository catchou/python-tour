from multiprocessing import Process
import os


print ('Process %s start...' % os.getpid())

def runProc(name):
    print('Run child process %s %s' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process: %s' % os.getpid())
    p = Process(target=runProc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')