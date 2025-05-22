from tkinter import *

window = Tk()  # instantiates an instance of a window
window.geometry("1300x700")
window.title("IT'S POPE JUICE!!!!!!!!!!!")

icon = PhotoImage(file='beetlejuice1.png')
window.iconphoto(True, icon)

window.config(background="black")

photo = PhotoImage(file='beetlejuice1.png')

label = Label(window, text="THAT AINT' GOT NOTHING TO DO WITH ME PAL",
              font=('Arial', 40, 'bold'),
              fg='green', bg='black',
              relief=RAISED,
              bd=10,
              padx=60,
              pady=60,
              image=photo,
              compound="bottom")

# label.place(x=100, y=100)
label.pack()

window.mainloop()
