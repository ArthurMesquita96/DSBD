from multiprocessing import Process
import time

def f(name):
    print('hello, sou', name)

if __name__ == '__main__':

    procs = []
    n_process = 5

    for i in range(n_process):
        p = Process(target=f, args=(f'bob filho {i}',))
        procs.append(p)

    print('hello, sou bob pai')
    
    for i in range(n_process):
        print(f'Criando processo {i}')
        procs[i].start()

    for i in range(5):
        procs[i].join()

