import tkinter as tk
from tkinter import ttk

# For a better text resolution
try:
	from ctypes import windll
	windll.shcore.SetProcessDpiAwareness(1)
except:
	pass

root = tk.Tk()
root.title('Greeter')
root.columnconfigure(0, weight=1)


frame1 = ttk.Frame(root, padding=(20, 10, 20, 0))
frame1.grid(row=0, column=0, sticky='EW')
frame1.columnconfigure(1, weight=1)

name_label = ttk.Label(frame1, text='Name')
name_label.grid(row=0, column=0, padx=(0, 10))

name_var = tk.StringVar()
input_box = ttk.Entry(frame1, width=20, textvariable=name_var)
input_box.grid(row=0, column=1, sticky='EW')


frame2 = ttk.Frame(root, padding=(20, 10))
frame2.grid(row=1, column=0, sticky='EW')
frame2.columnconfigure((0, 1) , weight=1)

grid_button = ttk.Button(frame2, text='Greet', command=(lambda : print(f"Hello {name_var.get() or 'World'}!")))
grid_button.grid(row=0, column=0, sticky='EW', padx=(0, 10))

quit_button = ttk.Button(frame2, text="Quit", command=root.destroy)
quit_button.grid(row=0, column=1, sticky='EW')

root.mainloop()