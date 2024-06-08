import concurrent.futures as cf


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

if __name__ == '__main__':
    with cf.ProcessPoolExecutor(16) as ex:
        zadania = [10_000] + [100] * 100
        # for w in ex.map(n_times_fibo, zadania):
        #     print(w)

        for r in cf.as_completed([ex.submit(n_times_fibo, n) for n in zadania]):
            print(r.result())
