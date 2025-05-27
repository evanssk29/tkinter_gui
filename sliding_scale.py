from tkinter import *
from tkinter.constants import HORIZONTAL


def submit():
    print("The Temperature is: "+str(scale.get())+ " degrees C")

window = Tk()

hotImage = PhotoImage(file='drew_natural.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window, from_=100,
              to=0,
              length=600,
              orient = VERTICAL, #orientation of scale
              font=('Consolas',20), # font for scale
              tickinterval=10, # adds numeric indicators for value
              # showvalue=5,
              troughcolor='yellow',
              fg='red',
              bg='black'

              )


scale.set(((scale['from']-scale['to']))/2+scale['to'])

scale.pack()

coldImage = PhotoImage(file='PNGgoLondon.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.mainloop()