import tkinter as tk

root = tk.Tk()

root.title('First Normal GUI')
root.geometry('800x500')

label = tk.Label(root, text='Hello World!', font=('Arial', 18))
label.pack(padx=20, pady=20) # pad = padding

textbox = tk.Text(root, font=('Arial', 16), height=3) # height 3 = height = to three lines
textbox.pack(padx=10, pady=10)

buttonframe = tk.Frame(root);
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='1', font=('Arial', 18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E) # n = north | s = south | w = west | e = east or without string tk.W+tk.E <-- west east

btn2 = tk.Button(buttonframe, text='2', font=('Arial', 18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E) # n = north | s = south | w = west | e = east or without string tk.W+tk.E <-- west east

btn3 = tk.Button(buttonframe, text='3', font=('Arial', 18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E) # n = north | s = south | w = west | e = east or without string tk.W+tk.E <-- west east

btn4 = tk.Button(buttonframe, text='4', font=('Arial', 18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E) # n = north | s = south | w = west | e = east or without string tk.W+tk.E <-- west east

btn5 = tk.Button(buttonframe, text='5', font=('Arial', 18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E) # n = north | s = south | w = west | e = east or without string tk.W+tk.E <-- west east

btn6 = tk.Button(buttonframe, text='6', font=('Arial', 18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E) # n = north | s = south | w = west | e = east or without string tk.W+tk.E <-- west east

anotherbutton = tk.Button(root, text='TEST')
anotherbtn.place(x=200, y=280, height=100, width=100) # .place() === position absolute


buttonframe.pack(fill='x') # its gonna make it strech in x direction

# button = tk.Button(root, text='Click Me', font=('Arial', 18))
# button.pack(padx=10, pady=10)


root.mainloop()
