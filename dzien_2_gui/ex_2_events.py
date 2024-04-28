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
    b1 = ttk.Button(root, text='Click Me!')
    def f1(event):
        print(event)

    def f2(event):
        print('Drugi handler.')

    b1.bind('<Return>', f1)
    b1.bind('<Return>', f2, add='+')
    # b1.focus()
    label.pack()
    b1.pack()
    root.mainloop()
