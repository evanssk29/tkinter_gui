from tkinter import *
from tkinter import colorchooser

def click():
    window.config(bg=colorchooser.askcolor()[1]) # changes background color

window = Tk()

window.geometry('420x420')
button = Button(text='Click Me',command=click)
button.pack()

window.mainloop()