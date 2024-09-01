import time
from multiprocessing import Process, active_children

def pi_naive(start, end, step, w):
    sum = 0.0

    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)

    return print(f'Processo {w}: {sum * step}')

if __name__ == "__main__":
    num_steps = 100000000 #10.000.000 (10+e7)
    sums = 0.0
    step = 1.0/num_steps
    n_workers = 4
    loop_range = num_steps/n_workers

    procs = []
    for i in range(n_workers):
        inicio = int(i * loop_range)
        fim = int((i + 1) * loop_range)

        p = Process(target=pi_naive, args=(inicio, fim, step, i))
        procs.append(p)

    print('Soma de cada processo:')
    tic = time.time() # Tempo Inicial
    for i in range(n_workers):
        procs[i].start()

    for i in range(n_workers):
        procs[i].join()

    toc = time.time() # Tempo Final

    print ("Tempo Pi: %.8f s" %(toc-tic))