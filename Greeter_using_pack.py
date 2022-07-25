import tkinter as tk
from tkinter import ttk 

root = tk.Tk()
root.title("Greet")
frame1 = ttk.Frame(root)
name_label = ttk.Label(frame1, text="Name")
name_label.pack(side='left', padx=(0, 10))
name_variable = tk.StringVar()
name_field = ttk.Entry(frame1, width=15, textvariable=name_variable)
name_field.pack(side='left', fill='x', expand=True)
name_field.focus()
frame1.pack(fill='x', padx=(10, 10), pady=(10, 10))

frame2 = ttk.Frame(root)
greet = ttk.Button(frame2, text="Greet", command=lambda : print(f"Hello {name_variable.get() or 'World'}!"))
greet.pack(side='left', expand=True, fill='x', padx=(0, 10))
exit = ttk.Button(frame2, text="Exit", command=root.destroy)
exit.pack(side='left', expand=True, fill='x')
frame2.pack(fill='x', padx=(10, 10), pady=(0, 10))
root.geometry("300x80")
root.mainloop()