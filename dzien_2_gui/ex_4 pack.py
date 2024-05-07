import tkinter as tk

root = tk.Tk()
root.title('Tkinter Pack Layout')
root.geometry('700x400+2200+100')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.columnconfigure(2, weight=2)
root.columnconfigure(3, weight=2)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=2)
root.rowconfigure(2, weight=2)

label1 = tk.Label(master=root, text='Tkinter', bg='red', fg='white')
label2 = tk.Label(master=root, text='Pack Layout', bg='green', fg='white')
label3 = tk.Label(master=root, text='Demo', bg='#333333', fg='white')

label1.grid(row=0, column=1, columnspan=3, sticky='nesw')
label2.grid(row=1, column=0, rowspan=3, sticky='nesw')
label3.grid(row=1, column=1, rowspan=2, columnspan=3, sticky='nesw')

root.mainloop()
