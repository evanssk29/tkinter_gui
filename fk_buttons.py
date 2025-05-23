from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("POPE JUICE")


photo = PhotoImage(file='beetlejuice1.png')
x = IntVar()

window.iconphoto(True, photo)

window.config(background="black")

def click(): # function to track clicks
    global count
    count += 1
    if count == 1:
        print("You voted for Pope Juice!!!!!")
    else:
        print("You voted for Pope Juice", count, "times!!")

button = Button(window,
                text="Click to vote for Pope Juice",
                command=click,
                font=("Comic Sans",15, 'bold'),
                fg='black', bg='red',
                activeforeground='red',
                activebackground='yellow',
                state=ACTIVE,
                image=photo,
                compound='left')

count = 0
button.pack(side=LEFT)

window.mainloop()