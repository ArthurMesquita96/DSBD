import time
from multiprocessing import Process


def pi_naive(start, end, step):
    print ("Start: ", str(start))
    print ("End: ", str(end))
    print ("Step: ", str(step))
    sum = 0.0

    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)
    return print(sum * step)

if __name__ == "__main__":
    num_steps = 10000000 #10.000.000 (10+e7)
    sums = 0.0
    step = 1.0/num_steps
    n_workers = 4
    loop_range = num_steps/n_workers

    procs = []
    for i in range(n_workers):
        inicio = int(i * loop_range)
        fim = int((i + 1) * loop_range)
        print(inicio)
        print(fim)
        print(step)

        p = Process(target=pi_naive, args=(inicio, fim, step,))
        procs.append(p)

    tic = time.time() # Tempo Inicial
    # sums = pi_naive(0, num_steps, step)
    for i in range(n_workers):
        procs[i].start()
    
    for i in range(n_workers):
        procs[1].join()

    toc = time.time() # Tempo Final

    # pi = step * sums
    # print ("Valor Pi: %.10f" %pi)
    # print ("Tempo Pi: %.8f s" %(toc-tic))