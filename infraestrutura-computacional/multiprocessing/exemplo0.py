from multiprocessing import Process
import time

def f(name):
    print('hello, sou', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob filho',))
    p.start()
    p.join()