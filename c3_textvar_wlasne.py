# Wziąć ex3 i dodać funkcjonalność taką że wpisany tekst w Entry po kliknięciu na buzik
# jest kopiowany do label'a
import time
import tkinter as tk
from tkinter import ttk


class MyStringVar(tk.StringVar):
    def __init__(self, org: tk.StringVar, szablon):
        super().__init__()
        self.org = org
        self.szablon = szablon
        self.org.trace_add('write', self.set_1)

    def set_1(self, *args, **kwargs):
        self.set(self.szablon.format(self.org.get()))


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
    t1 = tk.StringVar(value='w początkowa')
    t2 = MyStringVar(t1, 'Label: {}')
    label = ttk.Label(root, textvariable=t2)
    b1 = ttk.Button(root, text='Click Me!')
    e1 = ttk.Entry(root, textvariable=t1)
    # def f2(event):
    #     print('Drugi handler.', e1.get())
    #     label['text'] = e1.get()

    # b1.bind('<Button>', f2)
    # b1.focus()
    label.pack()
    e1.pack()
    b1.pack()
    root.mainloop()
