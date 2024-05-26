import multiprocessing
import timeit

import requests


# napisać funkcję cpu-heavy i spróbować ją uruchomić w n watkach
# zaobserwować brak skalowania

# 1 1 2 3 5 8 13 21 ...

def dos(n):
    url = 'https://gatling.io/'
    for _ in range(n):
        r = requests.get(url)
        # if r.status_code != 200:
        #     print(r.status_code)


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


def uruchom_w_procesach(funkcja, laczna_ilosc_operacji, ilosc_procesow):
    op_na_proces = laczna_ilosc_operacji // ilosc_procesow
    lista_procesow = []
    for _ in range(ilosc_procesow):
        lista_procesow.append(multiprocessing.Process(target=funkcja, args=(op_na_proces,)))
    for t in lista_procesow:
        t.start()
    for t in lista_procesow:
        t.join()


if __name__ == '__main__':
    x = [8, 16, 24, 32]
    for i in x:
        t = timeit.timeit(f'uruchom_w_procesach(n_times_fibo, 160_000, {i})',
                          number=1,
                          globals=globals(),
                          )
        print(f'{i}: {t:.2f} s.')
