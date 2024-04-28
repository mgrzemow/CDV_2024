# Napisać aplikację do przeliczania walut:
# Wizualne elementy:
# 1. Pole tekstowe z kwotą
# 2. Wybór waluty
# 3. Label, który wyświetli kwotę wg kursu.
# 4. Button uruchamiający obliczenia
# skąd kursy? Z API NBP:
# https://api.nbp.pl/api/exchangerates/tables/a/?format=json
import requests
r = requests.get('https://api.nbp.pl/api/exchangerates/tables/a/?format=json')
j = r.json()
print(j[0]['rates'][0]['mid'])


