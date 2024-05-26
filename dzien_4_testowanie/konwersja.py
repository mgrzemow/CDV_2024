import json

import requests
import random


class Konwerter:
    def __init__(self):
        j = requests.get('https://api.nbp.pl/api/exchangerates/tables/a/?format=json').json()
        # j = requests.get('asdasdasdasdasdsa').json()
        self.kursy = {d['code'].lower(): d['mid'] for d in j[0]['rates']}

    def konwertuj(self, waluta, kwota):
        return round(self.kursy[waluta.lower()] * kwota, 2)



if __name__ == '__main__':
    dane = []
    k = Konwerter()
    waluty = list(k.kursy.keys())
    for _ in range(100):
        kwota_w = random.randint(10000, 1_000_000) / 100
        waluta = random.choice(waluty)
        kwota_pln = k.konwertuj(waluta, kwota_w)
        dane.append(((waluta, kwota_w), kwota_pln))
        with open('dane_kursy.json', 'wt') as f:
            json.dump(dane, f, indent=2)
