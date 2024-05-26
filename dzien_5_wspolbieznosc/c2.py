import functools
# napisać funkcję cpu-heavy i spróbować ją uruchomić w n watkach
# zaobserwować brak skalowania

# 1 1 2 3 5 8 13 21 ...

@functools.lru_cache()
def fibo(n):
    x1 = 1
    x2 = 1
    tak dlugo jak nie dojde do konca:
        x3 = x1 + x2
        przsun wartosci w lewo
def n_times_fibo(n):
    for _ in range(n):
        fibo(10_000)

def uruchom_w_watkach(funkcja, laczna_ilosc_operacji, ilosc_watkow):
    ...
