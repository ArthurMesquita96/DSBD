import time
import numpy as np
from multiprocessing import Pool

def pi_naive(ranges):
    sum = 0.0

    for i in range(ranges[0], ranges[1]):
        x = (i+0.5) * ranges[2]
        sum = sum + 4.0/(1.0+x*x)

    return sum * ranges[2]

if __name__ == "__main__":
    num_steps = 100000000 #10.000.000 (10+e7)
    sums = 0.0
    step = 1.0/num_steps
    n_workers = 4
    loop_range = num_steps/n_workers

    p = Pool(n_workers)

    list_ranges = list()
    for i in range(n_workers):
        inicio = int(i * loop_range)
        fim = int((i + 1) * loop_range)
        list_ranges.append([inicio, fim, step])

    tic = time.time() # Tempo Inicial

    resultado = p.map(pi_naive, list_ranges)

    toc = time.time() # Tempo Final

    print ("Valor Pi: %.10f" %sum(resultado))
    print ("Tempo Pi: %.8f s" %(toc-tic))