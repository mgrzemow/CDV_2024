import time

import requests
koszyk = [
    ['usd', 1000],
    ['nzd', 222],
    ['eur', 444],
    ['chf', 555],
] * 100

def licz_koszyk(koszyk):
    suma = 0
    for waluta, kwota in koszyk:
        kurs = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/a/{waluta}/?format=json').json()['rates'][0]['mid']
        suma = round(kurs * kwota + suma, 2)
    return suma

def licz_w_watkach(koszyk, lista_wynikow):
    lista_wynikow.append(licz_koszyk(koszyk))

def licz_koszyk_na_watkach(koszyk, n_watkow):
    # podzielić dane wejściowe na n_watków
    # odpalic funkcję licz koszyk dla każdej paczki danych
    # policzyć sumę i zwrócić
    ...

if __name__ == '__main__':
    t1 = time.perf_counter()
    print(licz_koszyk(koszyk))
    print(f'Koszyk {len(koszyk)}: {time.perf_counter() - t1:.2f} s.')