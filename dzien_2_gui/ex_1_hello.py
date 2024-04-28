import time
import tkinter as tk
from tkinter import ttk

# opcjonalnie
# from tkinter import *
# from tkinter.ttk import *

if __name__ == '__main__':
    t1 = time.perf_counter()
    try:
        from ctypes import windll

        windll.shcore.SetProcessDpiAwareness(1)
    except:
        ...
    root = tk.Tk()
    root.title('Tytuł okienka...')
    # do wyliczania wstępnej pozycji okna
    print(f'Rozdzielczość: {root.winfo_screenwidth()} x {root.winfo_screenheight()}')
    # szerokoscxwysokosc+x_offset+y_offset
    root.geometry('700x400+5000+1000')

    # jak zabronić zmiany rozmiaru
    # root.resizable(False, False)

    # min i max size
    root.minsize(700, 400)
    root.maxsize(1400, 800)

    # przezroczystość
    # root.attributes('-alpha', .5)

    # na wierzchu
    # root.attributes('-topmost', 1)

    label = ttk.Label(root, text='Hello world!')
    label['text'] = 'New Hello!'
    label.config(text='Third hello!!!')


    # root.lower()
    # time.sleep(3)
    # root.lift()

    # root.lift(another_window)
    # root.lower(another_window)

    # Brak parametrów wejściowych
    # def b1_command():
    #     global t1
    #     t2 = time.perf_counter()
    #     label['text'] = f'Czas: {t2 - t1:.2f} s.'
    #     t1 = t2
    #     print('Button clicked!')
    # b1 = ttk.Button(root, text='Click Me!', command=b1_command)

    # Funkcja pośrednia - często lambda

    # def b1_command(przedrostek):
    #     global t1
    #     t2 = time.perf_counter()
    #     label['text'] = f'{przedrostek} Czas: {t2 - t1:.2f} s.'
    #     t1 = t2
    #     print('Button clicked!')
    #
    # b1 = ttk.Button(root, text='Click Me!', command=lambda: b1_command('Prefix:'))

    # Funkcja pośrednia - funkcja zwracająca funkcję
    def b1_command(przedrostek):
        def f1():
            global t1
            t2 = time.perf_counter()
            label['text'] = f'{przedrostek} Czas: {t2 - t1:.2f} s.'
            t1 = t2
            print('Button clicked!')

        return f1


    b1 = ttk.Button(root, text='Click Me!', command=b1_command('Prefix:'))

    label.pack()
    b1.pack()
    root.mainloop()
