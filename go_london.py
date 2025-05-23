from tkinter import *

def display():
    if x.get()==1:
        print("You will go London")
    else:
        print("You are a POS")

window = Tk()
window.config(background="black")

go_london = PhotoImage(file='PNGgoLondon.png')
window.geometry("500x500")
window.title("GO LONDON?")
window.iconphoto(True, go_london)
photo = PhotoImage(file='PNGgoLondon.png')
x = IntVar()

check_button = Checkbutton(window,
                           text="Will U go London?",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='red',
                           bg='black',
                           activeforeground='yellow',
                           activebackground='red',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound='left')
check_button.pack(side=LEFT)

window.mainloop()