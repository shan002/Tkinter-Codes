import tkinter as tk
from tkinter import ttk 


def calculate_namta():
	number = int(input_var.get())
	namta_output.delete('1.0', 'end')
	for i in range(1, 11):
		line = f"{number} x {i} = {number*i}\n"
		namta_output.insert(tk.END, line, 'center')

root = tk.Tk()
root.geometry('600x700')
root.title('Namta Generator')

input_frame = ttk.Frame(root, padding=(10, 10))
input_frame.pack()

input_var = tk.StringVar()
input_box = ttk.Entry(input_frame, textvariable=input_var, justify='center')
input_box.pack(side='left', padx=(0, 10))
input_box.focus()

calculate_button = tk.Button(input_frame, text='Calculate', bg='orange', relief=tk.RAISED, command=calculate_namta)
calculate_button.pack(side='left')

namta_output = tk.Text(root, width=20, height=14, font=('papyrus', 30), bg='black', fg='white')
namta_output.tag_config('center', justify='center')
namta_output.pack()

root.mainloop()