from tkinter import *
from tkinter.ttk import *
from tkcalendar import Calendar


from LookupExercise import LookupExercise
from CreateExercise import CreateExercise
from CreateRoutine import CreateRoutine
from LookupRoutine import LookupRoutine
from Calendar import BuildCalendar
from Home import HomePage


root = Tk()
root.title("TK Fitness")
root.geometry("800x600")

mainFrame = Frame(root, height=800, width=800)
mainFrame.grid_propagate(0)
mainFrame.grid()

def destroy():
    for widget in mainFrame.winfo_children():
        widget.destroy()

def createExercise():
    destroy()
    creatEx=Frame(mainFrame, height=600, width=800, relief=SUNKEN, borderwidth=5)
    creatEx.grid_propagate(0)
    creatEx.grid(row=0, column=0)
    CreateExercise(creatEx)

def lookupExercise():
    destroy()
    lookupEx=Frame(mainFrame, height=600, width=800, relief=SUNKEN, borderwidth=5)
    lookupEx.grid_propagate(0)
    lookupEx.grid(row=0, column=0)
    LookupExercise(lookupEx)

def createRoutine():
    destroy()
    createRout=Frame(mainFrame, height=600, width=800, relief=SUNKEN, borderwidth=5)
    createRout.grid_propagate(0)
    createRout.grid(row=0, column=0)
    CreateRoutine(createRout)

def updateRoutine():
    destroy()
    editRout = Frame(mainFrame, height=600, width=800, relief=SUNKEN, borderwidth=5)
    editRout.grid_propagate(0)
    editRout.grid(row=0, column=0)
    LookupRoutine(editRout)
    
def homeFn():
    destroy()
    home = Frame(mainFrame,height=600, width=800, relief=SUNKEN, borderwidth=5)
    home.grid_propagate(0)
    home.grid(row=0, column=0)
    HomePage(home)

def createCalendar():
    destroy()
    cal = Frame(mainFrame, height=600, width=800, relief=SUNKEN, borderwidth=5)
    cal.grid_propagate(0)
    cal.grid(row=0, column=0)
    BuildCalendar(cal)

menubar = Menu(root)
home = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Home", menu=home)
home.add_command(label="Go Home", command=homeFn)

exercise = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Exercises", menu=exercise)
exercise.add_command(label="Create", command=createExercise)
exercise.add_command(label="Lookup", command=lookupExercise)

routine = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Routines", menu=routine)
routine.add_command(label="Create", command=createRoutine)
routine.add_command(label="Edit", command=updateRoutine)

calendar = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Calendar", menu=calendar)
calendar.add_command(label="View Calendar", command=createCalendar)

homeFn()
root.config(menu=menubar)
root.mainloop()