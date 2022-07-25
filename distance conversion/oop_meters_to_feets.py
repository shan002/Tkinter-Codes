import tkinter as tk
import tkinter.font as font
from tkinter import ttk


class DistanceConverter(tk.Tk):

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.title('Metres to Feets')
        metre_input_frame = MetresToFeets(self, padding=(20, 10))
        metre_input_frame.grid()

        self.bind('<Return>', metre_input_frame.calculate)
        self.bind('KP-Return', metre_input_frame.calculate)


class MetresToFeets(ttk.Frame):

    def __init__(self, container, **kargs):
        super().__init__(container, **kargs)

        self.metres_str = tk.StringVar()
        self.feets_str = tk.StringVar()

        ttk.Label(self, text='Metres:').grid(row=0, column=0, sticky='W')
        metres_entry = ttk.Entry(self, width=10, textvariable=self.metres_str, font=('Segoe UI', 15))
        metres_entry.grid(row=0, column=1, sticky='EW')
        metres_entry.focus()
        ttk.Label(self, text='Feets:').grid(row=1, column=0, sticky='W')
        ttk.Label(self, textvariable=self.feets_str).grid(row=1, column=1, sticky='W')
        ttk.Button(self, text='Calculate', command=self.calculate).grid(row=2, column=0, columnspan=2, sticky='EW')

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def calculate(self, *args):
        try:
            metres = float(self.metres_str.get())
            feets = metres * 3.28084
            self.feets_str.set(f'{feets:.3f}')
        except ValueError:
            pass


root = DistanceConverter()
root.eval('tk::PlaceWindow . center')  # To center the window on the computer screen
root.columnconfigure(index=0, weight=1)
font.nametofont('TkDefaultFont').config(size=15)
root.mainloop()
