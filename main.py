from tkinter import *

window = Tk()

window.title("My First Desktop App")
window.geometry("800x500")



lbl = Label(window, text="Hello World", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

txt = Entry(window, font=("Arial Bold", 10), justify='center', width=60)
txt.grid(column=0, row=1)

def gotClicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text=res)

btn = Button(window, text="Click Me", bg="red", fg="white", command=gotClicked)
disabledBtn = Button(window, text="Click Me", bg="red", fg="white", state='disabled')
btn.grid(column=1, row=0)
disabledBtn.grid(column=2, row=0)



window.mainloop()
