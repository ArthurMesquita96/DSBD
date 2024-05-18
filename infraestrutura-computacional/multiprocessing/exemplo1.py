from multiprocessing import Process
import time

def f(name, id):
    print('hello, sou', name, id)

if __name__ == '__main__':
    procs = []
    for i in range(4):
        p = Process(target=f, args=('bob filho',i,))
        procs.append(p)

    print('hello, sou', 'bob pai')

    for i in range(4):
        procs[i].start()
    for i in range(4):
        procs[i].join()
        # pass

    print('hello, sou', 'bob neto')
