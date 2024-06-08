import multiprocessing.pool
import time
import timeit

import requests


def fibo(n):
    x1 = 1
    x2 = 1
    while n > 2:
        x1, x2 = x2, x1 + x2
        n -= 1
    return x2


def n_times_fibo(n):
    for _ in range(n):
        fibo(10_000)
    return 'wynik'


class MojCallback:
    def __init__(self, name, total):
        self.name = name
        self.total = total
        self.done = 0
        self.results = []

    def all_done(self):
        return self.done == self.total

    def __call__(self, wynik):
        # zliczanie ilosci
        self.done += 1
        # zbieranie wynikow??
        self.results.append(wynik)

    def __repr__(self):
        return f'{self.name} {self.done} / {self.total} ...'


if __name__ == '__main__':
    with multiprocessing.pool.Pool(8) as pool:
        # w = pool.apply(n_times_fibo, (100,))
        # print(w)
        # r = pool.apply_async(n_times_fibo, (1000,))
        # print(r)
        # while not r.ready():
        #     print('Still waiting...')
        #     time.sleep(1)
        # print(r.get())

        # zadania = [100] * 100
        # wyniki = pool.map(n_times_fibo, zadania)
        # print(wyniki)
        #
        # zadania = [100] * 100
        # r = pool.map_async(n_times_fibo, zadania)
        # while not r.ready():
        #     print('Still waiting...')
        #     time.sleep(1)
        # print(r.get())
        #
        # zadania = [(100,)] * 100
        # r = pool.starmap_async(n_times_fibo, zadania)
        # while not r.ready():
        #     print('Still waiting...')
        #     time.sleep(1)
        # print(r.get())
        zadania = [100] * 100
        # lista_taskow = [pool.apply_async(n_times_fibo, (p,)) for p in zadania]
        # while not all(t.ready() for t in lista_taskow):
        #     done = sum(1 for t in lista_taskow if t.ready())
        #     print(f'Done {done} / {len(lista_taskow)}...')
        #     time.sleep(1)
        # print([t.get() for t in lista_taskow])
        #
        mc = MojCallback('Przykładowa paczka zadań', len(zadania))
        lista_taskow = [pool.apply_async(n_times_fibo, (p,), callback=mc) for p in zadania]
        while not mc.all_done():
            print(mc)
            time.sleep(1)
        print(mc.results)
