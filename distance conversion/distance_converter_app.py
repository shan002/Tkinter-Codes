import tkinter as tk
import tkinter.font as font
from tkinter import ttk


class DistanceConverter(tk.Tk):

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.title('Distance Converter')
        self.columnconfigure(0, weight=1)
        container = tk.Frame(self, bg='blue')
        container.grid()

        self.frames = dict()

        for Frame in (MetresToFeets, FeetsToMetres):
            frame = Frame(container, self, padding=(32, 10))
            frame.grid(row=0, column=0, sticky='nsew')
            frame.columnconfigure(1, weight=2)
            self.frames[Frame] = frame

        self.show_frame(MetresToFeets)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        frame.input_box.focus()
        frame.input_str.set('')
        frame.output_str.set('')
        self.bind('<Return>', frame.calculate)
        self.bind('KP-Return', frame.calculate)


class MetresToFeets(ttk.Frame):

    def __init__(self, container, controller, **kargs):
        super().__init__(container, **kargs)

        self.input_str = tk.StringVar()
        self.output_str = tk.StringVar()

        ttk.Label(self, text='Metres:').grid(row=0, column=0, sticky='W')
        self.input_box = ttk.Entry(self, width=10, textvariable=self.input_str, font=('Segoe UI', 15))
        self.input_box.grid(row=0, column=1, sticky='EW')
        ttk.Label(self, text='Feets:').grid(row=1, column=0, sticky='W')
        ttk.Label(self, textvariable=self.output_str).grid(row=1, column=1, sticky='W')
        ttk.Button(self, text='Calculate', command=self.calculate).grid(row=2, column=0, columnspan=2, sticky='EW')
        ttk.Button(
            self,
            text='Switch to feets conversion',
            width=25,
            command=lambda: controller.show_frame(FeetsToMetres)).grid(row=3, column=0, columnspan=2, sticky='EW')

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def calculate(self, *args):
        try:
            metres = float(self.input_str.get())
            feets = metres * 3.28084
            self.output_str.set(f'{feets:.3f}')
        except ValueError:
            pass


class FeetsToMetres(ttk.Frame):

    def __init__(self, container, controller, **kargs):
        super().__init__(container, **kargs)

        self.input_str = tk.StringVar()
        self.output_str = tk.StringVar()

        ttk.Label(self, text='Feets:').grid(row=0, column=0, sticky='W')
        self.input_box = ttk.Entry(self, width=10, textvariable=self.input_str, font=('Segoe UI', 15))
        self.input_box.grid(row=0, column=1, sticky='EW')
        ttk.Label(self, text='Metres:').grid(row=1, column=0, sticky='W')
        ttk.Label(self, textvariable=self.output_str).grid(row=1, column=1, sticky='W')
        ttk.Button(self, text='Calculate', command=self.calculate).grid(row=2, column=0, columnspan=2, sticky='EW')
        ttk.Button(
            self,
            text='Switch to metres conversion',
            command=lambda: controller.show_frame(MetresToFeets)).grid(row=3, column=0, columnspan=2, sticky='EW')

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def calculate(self, *args):
        try:
            feets = float(self.input_str.get())
            metres = feets / 3.28084
            self.output_str.set(f'{metres:.3f}')
        except ValueError:
            pass


root = DistanceConverter()
root.eval('tk::PlaceWindow . center')  # To center the window on the computer screen
font.nametofont('TkDefaultFont').config(size=15)
root.mainloop()
