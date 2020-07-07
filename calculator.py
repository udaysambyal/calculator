
import tkinter
from tkinter import *


def click(event):
    global data
    global lbl
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        if data.get().isdigit():
            value = int(data.get())
        else:
            value = eval(data.get())

        data.set(value)
        lbl.update()


    elif text == "c":
        data.set("")
        lbl.update()
    else:
        data.set(data.get() + text)
        lbl.update()



root = tkinter.Tk()
root.geometry("250x400")
root.resizable(0,0)
root.title("Calculator")

data = StringVar()
data.set("")
lbl =Label(
    root,
    text = "",
    anchor = SE,
    font = ("Verdana" ,20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000"
)
lbl.pack(expand = True, fill = "both")


btnrow1 = Frame(root,bg = "#000000")
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")


btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn1.pack(side = LEFT, expand =True, fill = "both")
btn1.bind("<Button-1>",click)

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn2.pack(side = LEFT, expand =True, fill = "both")
btn2.bind("<Button-1>",click)

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn3.pack(side = LEFT, expand =True, fill = "both")
btn3.bind("<Button-1>",click)

btn4 = Button(
    btnrow1,
    text = "+",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn4.pack(side = LEFT, expand =True, fill = "both")
btn4.bind("<Button-1>",click)

btn1 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn1.pack(side = LEFT, expand =True, fill = "both")
btn1.bind("<Button-1>",click)

btn2 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn2.pack(side = LEFT, expand =True, fill = "both")
btn2.bind("<Button-1>",click)

btn3 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn3.pack(side = LEFT, expand =True, fill = "both")
btn3.bind("<Button-1>",click)

btn4 = Button(
    btnrow2,
    text = "-",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn4.pack(side = LEFT, expand =True, fill = "both")
btn4.bind("<Button-1>",click)


btn1 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn1.pack(side = LEFT, expand =True, fill = "both")
btn1.bind("<Button-1>",click)

btn2 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn2.pack(side = LEFT, expand =True, fill = "both")
btn2.bind("<Button-1>",click)

btn3 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn3.pack(side = LEFT, expand =True, fill = "both")
btn3.bind("<Button-1>",click)

btn4 = Button(
    btnrow3,
    text = "*",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn4.pack(side = LEFT, expand =True, fill = "both")
btn4.bind("<Button-1>",click)


btn1 = Button(
    btnrow4,
    text = "c",
    font = ("Verdana", 22),
    border = 0
)
btn1.pack(side = LEFT, expand =True, fill = "both")
btn1.bind("<Button-1>",click)

btn2 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn2.pack(side = LEFT, expand =True, fill = "both")
btn2.bind("<Button-1>",click)

btn3 = Button(
    btnrow4,
    text = "=",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn3.pack(side = LEFT, expand =True, fill = "both")
btn3.bind("<Button-1>",click)

btn4 = Button(
    btnrow4,
    text = "/",
    font = ("Verdana", 22),
    relief = GROOVE,
    border = 0
)
btn4.pack(side = LEFT, expand =True, fill = "both")
btn4.bind("<Button-1>",click)

root.mainloop()


'''
import tkinter
from tkinter import *
master = Tk()

# Create this method before you create the entry
def return_entry():
    """Gets and prints the content of the entry"""
    content = entry.get()
    print(content)  

Label(master, text="Input: ").grid(row=0, sticky=W)

entry = Entry(master)
entry.grid(row=0, column=1)

# Connect the entry with the return button
#entry.bind('<Return>', return_entry)
button=Button(text="Click",command=return_entry).grid(row=1,sticky=W)


mainloop()
'''

'''
import tkinter as tk
from tkinter import *

window=tk.Tk()
#greet=tk.Label(text="Welcome")
#greet.pack()
#window.mainloop()
def command():
    print(name)
greet=tk.Label(window,text="Welcome").grid(row=0,column=0)
e1=tk.Entry().grid(row=0,column=1)
name = e1.get()

greet2=tk.Label(window,text="Name").grid(row=1,column=0)
e2=tk.Entry().grid(row=1,column=1)

b1=tk.Button(window,text="Click Me",bg='red',fg='yellow',command=command).grid(row=2,column=1)


window.mainloop()

'''