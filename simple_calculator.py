import tkinter as tk 
from tkinter import ttk 

def add(number1: str, number2: str) -> str:
	number1 = int(number1) if number1 else 0
	number2 = int(number2) if number2 else 0
	root.geometry('300x150')
	return str(number1 + number2)

def subtract(number1: str, number2: str) -> str:
	number1 = int(number1) if number1 else 0
	number2 = int(number2) if number2 else 0
	root.geometry('300x150')
	return str(int(number1) - int(number2))

def multiply(number1: str, number2: str) -> str:
	number1 = int(number1) if number1 else 0
	number2 = int(number2) if number2 else 0
	root.geometry('300x150')
	return str(int(number1) * int(number2))

def divide(number1: str, number2: str) -> str:
	number1 = int(number1) if number1 else 0
	number2 = int(number2) if number2 else 1
	if number2:
		root.geometry('300x150')
	else:
		root.geometry('700x150')
	return str(int(int(number1) / int(number2))) if number2 else 'CAN NOT DIVIDE BY ZERO'

def show_answer(answer_str: str):
	answer.delete('1.0', 'end')
	answer.insert(tk.END, answer_str, 'center')

root = tk.Tk()
root.geometry('300x150')
root.title('Jog Biyog Gun Vaag')
root.columnconfigure(0, weight=1)

input_frame = ttk.Frame(root, padding=(10, 10, 10, 10))
input_frame.grid(row=0, column=0, sticky='EW')
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)

input1_var = tk.StringVar()
input1 = ttk.Entry(input_frame, textvariable=input1_var, justify='center')
input1.grid(row=0, column=0, sticky='EW', padx=(0, 10))
input1.focus()

input2_var = tk.StringVar()
input2 = ttk.Entry(input_frame, textvariable=input2_var, justify='center')
input2.grid(row=0, column=1, sticky='EW')

button_frame = ttk.Frame(root, padding=(10, 0, 10, 10))
button_frame.grid(row=1, column=0)

add_button = tk.Button(button_frame, text='ADD', command=( lambda : show_answer(add(input1.get(), input2.get()))), 
	bg='red', relief=tk.RAISED)
add_button.grid(row = 0, column=0, padx=(0, 10))
subtract_button = tk.Button(button_frame, text='SUBTRACT', command=( lambda : show_answer(subtract(input1.get(), input2.get()))), 
	bg='green', relief=tk.RAISED)
subtract_button.grid(row = 0, column=1, padx=(0, 10))
multiply_button = tk.Button(button_frame, text='MULTIPLY', command=( lambda : show_answer(multiply(input1.get(), input2.get()))), 
	bg='blue', relief=tk.RAISED)
multiply_button.grid(row = 0, column=2, padx=(0, 10))
divide_button = tk.Button(button_frame, text='DIVIDE', command=( lambda : show_answer(divide(input1.get(), input2.get()))), 
	bg='orange', relief=tk.RAISED)
divide_button.grid(row = 0, column=3)

answer = tk.Text(root, width=10, height=1, font=("Helvetica", 32))
answer.tag_config('center', justify='center')
answer.grid(row=2, column=0, sticky='EW', padx=(10, 10), pady=(0, 10))


root.mainloop()