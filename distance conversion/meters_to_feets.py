import tkinter as tk
import tkinter.font as font
from tkinter import ttk


def calculate(*args):
    try:
        metres = float(metres_str.get())
        feets = metres * 3.28084
        feets_str.set(f'{feets:.3f}')
    except ValueError:
        pass


root = tk.Tk()
root.title('Metres to Feets')
root.eval('tk::PlaceWindow . center')  # To center the window on the computer screen
root.columnconfigure(index=0, weight=1)

metres_str = tk.StringVar()
feets_str = tk.StringVar()

default_font = font.nametofont('TkDefaultFont')
default_font.config(size=15)

main = ttk.Frame(root, padding=(20, 10))
main.grid()

ttk.Label(main, text='Metres:').grid(row=0, column=0, sticky='W')
metres_entry = ttk.Entry(main, width=10, textvariable=metres_str, font=default_font)
metres_entry.grid(row=0, column=1, sticky='EW')
metres_entry.focus()
ttk.Label(main, text='Feets:').grid(row=1, column=0, sticky='W')
ttk.Label(main, textvariable=feets_str).grid(row=1, column=1, sticky='W')
ttk.Button(main, text='Calculate', command=calculate).grid(row=2, column=0, columnspan=2, sticky='EW')

for child in main.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind('<Return>', calculate)
root.bind('KP-Return', calculate)

root.mainloop()
