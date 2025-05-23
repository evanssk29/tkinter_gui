from tkinter import *


def submit(): # function for submit button
    user_name = entry.get()
    print("Hello", user_name)
    # entry.config(state=DISABLED) # disables entry box

# def click(): # function to track clicks
#     global count
#     count += 1
#     if count == 1:
#         print("You voted for Pope Juice!!!!!")
#     else:
#         print("You voted for Pope Juice", count, "times!!")

def delete(): # function to delete all
    entry.delete(0,END)

def backspace(): # function to delete one character
    entry.delete(len(entry.get())-1,END)

# def display():
#     if x.get()==1:
#         print("You will go London")
#     else:
#         print("You are a POS")

window = Tk()  # instantiates an instance of a window
window.geometry("1000x500")
window.title("******POPE JUICE******")

photo = PhotoImage(file='beetlejuice1.png')
go_london = PhotoImage(file='PNGgoLondon.png')
icon = PhotoImage(file='beetlejuice1.png')
x = IntVar()




entry = Entry(window,
              font=("Arial",20),
              fg="red",
              bg="black",
              show="*")
# entry.insert(0, 'Enter Text') # pre-entered text in entry box
entry.pack(side=BOTTOM)

submit_button = Button(window,text='submit',command=submit)
submit_button.pack(side=BOTTOM)

# check_button = Checkbutton(window,
#                            text="Will U go London?",
#                            variable=x,
#                            onvalue=1,
#                            offvalue=0,
#                            command=display,
#                            font=('Arial',20),
#                            fg='red',
#                            bg='black',
#                            activeforeground='yellow',
#                            activebackground='red',
#                            padx=25,
#                            pady=10,
#                            image=go_london,
#                            compound='left')
# check_button.pack(side=LEFT)

delete_button = Button(window,text='delete',command=delete)
delete_button.pack(side=BOTTOM)

backspace_button = Button(window,text='backspace',command=backspace)
backspace_button.pack(side=BOTTOM)


window.iconphoto(True, icon)

window.config(background="black")

label = Label(window,
              text="THAT AINT' GOT NOTHING TO DO WITH ME PAL",
              font=('Arial', 20, 'bold'),
              fg='green', bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="bottom")
label.pack()
# label.place(x=100, y=100) # places label at certain cords


# button = Button(window,
#                 text="Click to vote for Pope Juice",
#                 command=click,
#                 font=("Comic Sans",15, 'bold'),
#                 fg='black', bg='red',
#                 activeforeground='red',
#                 activebackground='yellow',
#                 state=ACTIVE,
#                 image=photo,
#                 compound='left')
#
# count = 0
# button.pack()

window.mainloop()
