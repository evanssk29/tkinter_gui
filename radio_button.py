# radio button = similar to checkbox, but you can only select one from a group
from tkinter import *

senate = ["Pope Juice","Go London","Drew Natural"]

def votes():
    if(x.get())==0:
        print("You voted for Pope Juice!")
    elif(x.get()==1):
        print("You voted Go London Cat!")
    elif(x.get()==2):
        print("You voted for Drew Natural!")
    else:
        print("FUCK YOURSELF!")

window = Tk()
window.config(background="black")
window.geometry("600x700")
window.title("******CAST UR VOTE******")

label = Label(window,
              text="CAST UR VOTE!!",
              font=('Arial', 15, 'bold'),
              fg='red', bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              # compound="bottom"
              )
label.pack(anchor='w')

vote_pope = PhotoImage(file='beetlejuice1.png')
vote_london = PhotoImage(file='PNGgoLondon.png')
vote_drew = PhotoImage(file='drew_natural.png')
window.iconphoto(True, vote_drew)
senante_list = [vote_pope,vote_london, vote_drew]





x = IntVar()

for index in range(len(senate)):
    radiobutton = Radiobutton(window,
                              text=senate[index], # adds text to radio buttons
                              variable=x, # groups radiobuttons together if they share the same variable
                              value=index, # assigns each radiobutton a different value
                              padx=40,
                              font=("Impact",30),
                              fg="red",
                              bg="black",
                              image=senante_list[index], # adds image to radiobutton
                              compound='left', # adds image and text to left side
                              indicatoron=0,
                              width=375, # sets width of radiobuttons
                              command=votes) # sets command of radiobutton to function
    radiobutton.pack(anchor="w")

window.mainloop()
