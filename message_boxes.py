from tkinter import *

from tkinter import messagebox # imports message box library

def click():
    answer = messagebox.askyesnocancel(title='Yes no cancel',message='Do you like to code?',icon='warning')
    if(answer==True):
        print("You like to code")
    elif(answer == False):
        print("Then why are you watching a video on coding?")
    else:
        print("You have dodged the question")


    # answer = messagebox.askquestion(title='ask question',message='do you like pie?')
    # if(answer == 'yes'):
    #     print('I like pie too!')
    # else:
    #     print('Why do you not like pie?')
    # if messagebox.askyesno(title="ask yes or no",message="do you like cake? "):
    #     print('I like cake too!')
    # else:
    #     print('Why do you not like cake? ')
    # if messagebox.askretrycancel(title='ask ok cancel',message='Do you want to retry a thing? '):
    #     print("You retried a thing!")
    # else:
    #     print("You canceled a thing!")
    # if messagebox.askokcancel(title='ask ok cancel',message='Do you want to do the thing? '):
    #     print("You did a thing")
    # else:
    #     print("You canceled a thing")
    # messagebox.showerror(title='ERROR!',message="Something went wrong: ")
    # while(True):
    # messagebox.showwarning(title='WARNING!', message='You have a virus!')
    # messagebox.showinfo(title='This is an info message box',message='You are a person')

window = Tk()

button = Button(window,command=click,text="Click me")
button.pack()

window.mainloop()

