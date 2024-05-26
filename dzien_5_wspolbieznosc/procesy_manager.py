import multiprocessing
import timeit

import requests



def fibo(n):
    x1 = 1
    x2 = 1
    while n > 2:
        x1, x2 = x2, x1 + x2
        n -= 1
    return x2


def n_times_fibo(n, d):
    for _ in range(n):
        fibo(10_000)
    d[multiprocessing.current_process().name] = 'wynik'





if __name__ == '__main__':
    with multiprocessing.Manager() as m:
        d = m.dict()
        l = m.list()
        v = m.Value(int, 1)
        p1 = multiprocessing.Process(target=n_times_fibo, args=(1000, d))
        p2 = multiprocessing.Process(target=n_times_fibo, args=(1000, d))
        p3 = multiprocessing.Process(target=n_times_fibo, args=(1000, d))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
        print(d)