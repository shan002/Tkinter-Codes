import tkinter as tk

root = tk.Tk()

tk.Entry(root, bg='blue').grid(sticky='we')
root.grid_columnconfigure(0, weight=1)

root.mainloop()
