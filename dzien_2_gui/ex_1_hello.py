import time
import tkinter as tk
from tkinter import ttk


# opcjonalnie
# from tkinter import *
# from tkinter.ttk import *

if __name__ == '__main__':
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

    def b1_command():
        print('Button clicked!')

    b1 = ttk.Button(root, text='Click Me!', command=b1_command)

    label.pack()
    b1.pack()
    root.mainloop()
