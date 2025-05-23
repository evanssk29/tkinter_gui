from tkinter import *

def submit(): # function for submit button
    user_name = entry.get()
    print("Hello", user_name, "that ain't got nutin to do with me pal.")
    # entry.config(state=DISABLED) # disables entry box

def delete(): # function to delete all
    entry.delete(0,END)

def backspace(): # function to delete one character
    entry.delete(len(entry.get())-1,END)


window = Tk()  # instantiates an instance of a window
window.geometry("1000x500")
window.title("******POPE JUICE******")
photo = PhotoImage(file='beetlejuice1.png')

entry = Entry(window,
              font=("Arial",20),
              fg="red",
              bg="black")
              # show="*")
# entry.insert(0, 'Enter Text') # pre-entered text in entry box
entry.pack(side=TOP)

submit_button = Button(window,text='submit',command=submit)
submit_button.pack(side=BOTTOM)

delete_button = Button(window,text='delete',command=delete)
delete_button.pack(side=BOTTOM)

backspace_button = Button(window,text='backspace',command=backspace)
backspace_button.pack(side=LEFT)


window.iconphoto(True, photo)

window.config(background="black")

label = Label(window,
              text="THAT AINT' GOT NOTHING TO DO WITH ME PAL",
              font=('Arial', 20, 'bold'),
              fg='green', bg='black',
              relief=RAISED,
              bd=10,
              padx=10,
              pady=10,
              image=photo,
              compound="bottom")
label.pack(side=BOTTOM)

window.mainloop()
