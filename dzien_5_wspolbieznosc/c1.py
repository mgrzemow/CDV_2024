import threading
import time
import itertools
import requests

koszyk = [
             ['usd', 1000],
             ['nzd', 222],
             ['eur', 444],
             ['chf', 555],
             ['thb', 555],
             ['aud', 4444],
             ['cad', 666],
             ['huf', 666],
             ['gbp', 666],
             ['uah', 666],
             ['jpy', 666],
             ['CZK', 666],
             ['DKK', 666],
             ['ISK', 666],
             ['NOK', 666],
             ['SEK', 666],
         ] * 5


def licz_koszyk(koszyk):
    suma = 0
    for waluta, kwota in koszyk:
        r = requests.get(f'https://api.nbp.pl/api/exchangerates/rates/a/{waluta}/?format=json')
        r.raise_for_status()
        kurs = r.json()['rates'][0][
            'mid']
        suma = round(kurs * kwota + suma, 2)
    return suma


def licz_i_dodaj(koszyk, lista_wynikow):
    lista_wynikow.append(licz_koszyk(koszyk))


def licz_koszyk_na_watkach(koszyk, n_watkow):
    # podzielić dane wejściowe na n_watków
    wielkosc_koszyka = len(koszyk) // n_watkow + 1
    lista_koszykow = itertools.batched(koszyk, wielkosc_koszyka)
    lista_sum = []
    lista_watkow = []
    for k in lista_koszykow:
        t = threading.Thread(target=licz_i_dodaj, args=(k, lista_sum))
        t.start()
        lista_watkow.append(t)
    for t in lista_watkow:
        t.join()
    return sum(lista_sum)


if __name__ == '__main__':
    t1 = time.perf_counter()
    print(licz_koszyk_na_watkach(koszyk, 75))
    print(f'Koszyk {len(koszyk)}: {time.perf_counter() - t1:.2f} s.')
