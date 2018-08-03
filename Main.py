'''
Created on Jun 17, 2016

@author: michael.kleiman

a quick script I quickly made to reveal the details off fullscreen applications' mouse input handling 
(for example, if the program does not allow mouse acceleration to be fully disabled, 
or if it doesn't specify how to achieve my deisred 1:1 ratio of input:motion


'''
from pyautogui import *
from time import *
from tkinter import *

top = Tk()
#default values
xDefault = 1920
cDefault = 10
dDefault = 10
cancel = False
running = False

#clears the messagebox, inserts 'message', forces update
def newMessage(message, forceUpdate=False):
    messagebox.delete(1.0, END)                                                                 
    messagebox.insert(INSERT, message)
    if forceUpdate:
        messagebox.update()

#sets the text in the runButton
def setRunButtonText(text):
    runButton["text"] = text
    runButton.update()


#when the start button is clicked, this does the mouse movement
def start():
    global running
    global cancel
    #for canceling the run
    if running:
        cancel = True
        return
    try:
        x = xbox.get()
        if x is "":
            x = xDefault 
        else:
            x = int(x)#raises value error for non integer entries
        if x < 1:
            raise ValueError
    except ValueError:
        newMessage("enter only natural numbers in the distance field")
        return
    try:
        c = countbox.get()
        if c is "":
            c = cDefault 
        else:
            c = int(c)#raises value error for non integer entries
        if c < 1:
            raise ValueError
    except ValueError:
        newMessage("enter only natural numbers in the steps field")
        return
    try:
        d = delaybox.get()
        if d is "":
            d = dDefault
        else:
            d = int(d)#raises value error for non integer entries
        if d < 1:
            raise ValueError
    except ValueError:
        newMessage("enter only natural numbers in the delay field")
        return
    
    #now it runs
    running = True
    setRunButtonText("cancel")
    for i in range(d):
        if cancel:
            newMessage("", True) 
            cancel = False
            running = False
            setRunButtonText("start")
            return
        newMessage("running in " + str(d-i) + " seconds...", True)
        sleep(1)
    newMessage("running", True)
    j = (int)(x/c)
    setRunButtonText("")
    for i in range(c):
        if cancel:
            newMessage("", True)
            cancel = False
            running = False
            setRunButtonText("start")
            return
        moveRel(j, 0)
   
    k = (x/c * 0) - (2000*j)
    moveRel(x - (j*c), 0)#for the pixels lost by rounding`
    messagebox.delete(1.0, END)
    setRunButtonText("start")
    newMessage("done")
    running = False

frame = Frame(top, width=0, height=0)

runButton = Button(top, text = "start", command = start)
xboxLabel = Label(top, text = "x distance (optional, default is " + str(xDefault) + ")")
xbox = Entry(top, font = "Times", exportselection = 0)
countbox = Entry(top, font = "Times", exportselection = 0)
countboxLabel = Label(top, text = "number of steps for the run (optional, default is " + str(cDefault) + ")")
delayLabel = Label(top, text = "number of seconds to delay (default is " + str(dDefault) + ")")
delaybox = Entry(top, font = "Times", exportselection = 0)
messageLabel = Label(top, text = "messages:")
messagebox = Text(top, font = "Times", exportselection = 0, height = 1, width = 40)



xboxLabel.pack()
xbox.pack()
countboxLabel.pack()
countbox.pack()
delayLabel.pack()
delaybox.pack()
messageLabel.pack()
messagebox.pack()

runButton.pack()
frame.pack()
frame.focus_set()
top.mainloop()
