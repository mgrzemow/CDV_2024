# zmodyfikować poprzedni przykład, tak aby:
# - były 2 przyciski:
#    - tak jak do tej pory pomiar czasu
#    - czyści label

# Użyć jednj funkcji, która rozróżni który button został naciśnięty za pomocą klawisza Enter

import time
import tkinter as tk
from tkinter import ttk

if __name__ == '__main__':
    t1 = time.perf_counter()
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    except:
        ...
    root = tk.Tk()
    # szerokoscxwysokosc+x_offset+y_offset
    root.geometry('700x400+5000+1000')
    label = ttk.Label(root, text='Hello world!')
    b1 = ttk.Button(root, text='Stoper', name='b1')
    b2 = ttk.Button(root, text='Czyść!', name='b2')
    b2.state(['disabled'])


    def f1(event: tk.Event):
        if event.widget is b1:
            global t1
            t2 = time.perf_counter()
            label['text'] = f'Czas: {t2 - t1:.2f} s.'
            t1 = t2
            b2.state(['!disabled'])

        elif event.widget is b2:
            label['text'] = ''


    b1.bind('<Return>', f1)
    b1.bind('<Key-a>', f1)
    b1.bind('<Alt-c>', f1)
    b1.bind('<Button>', f1)
    b1.bind('<Button-1>', f1)
    b1.bind('<Enter>', f1)
    b1.bind('<Leave>', f1)

    b2.bind('<Return>', f1)
    b2.bind('<FocusIn>', f1)

    # bINDOWANIE DLA CAŁEJ KLASY WIDGETÓW:
    # root.bind_class('Button', '<Control-V>', paste)

    # b1.focus()
    label.pack()
    b1.pack()
    b2.pack()
    root.mainloop()
