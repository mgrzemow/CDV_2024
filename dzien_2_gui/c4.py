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
kursy = {d['code']: d['mid'] for d in j[0]['rates']}
# kursy = {}
# for d in j[0]['rates']:
#     kursy[d['code']] = d['mid']

import tkinter as tk
from tkinter import ttk


if __name__ == '__main__':
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    except:
        ...
    root = tk.Tk()
    # szerokoscxwysokosc+x_offset+y_offset
    root.geometry('700x400+5000+1000')
    root.title('Kursy walut')
    e1 = ttk.Entry()
    c1 = ttk.Combobox(values=list(kursy.keys()))
    b1 = ttk.Button(root, text='Wylicz kurs')
    label = ttk.Label(root, text='')
    def f1(event):
        print(event)

    b1.bind('<Button>', f1)
    # b1.focus()
    e1.pack()
    c1.pack()
    b1.pack()
    label.pack()
    root.mainloop()

