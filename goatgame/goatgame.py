from tkinter import *
import tkinter
from PIL import ImageTk,Image


templist = []
playerlist = []

def howManyPlayers():
    global entry, amountOfPlayers
    amountOfPlayers = entry.get()
    if int(amountOfPlayers) > 108:
        howManyPlayersLabel.configure(text="Amount of players cant be more than 108!")
    else:
        numOfPlayers.destroy()
        window.lift()
        generateEntries()

def generateXandY():
    global x,y, templist
    x = -1
    y = 0
    for a in range (0,int(amountOfPlayers)):
        if x == 8:
            y += 1
            x = 0
        else:
            x += 1
        entry = tkinter.Entry(entrywindow, width=20)
        entry.grid(row=y, column=x, padx= 20, pady= 20)
        templist.append(entry)

    nextbutton2 = tkinter.Button(entrywindow, text="Next", command=placeinplayerlist)
    nextbutton2.grid(column=4,row=12)

def placeinplayerlist():
    global img
    for x in templist:
        playerlist.append(x.get())
    print(playerlist)
    entrywindow.destroy()
    gamewindow = Toplevel(window)
    gamewindow.geometry("2000x1000")
    gamewindow.title("Goat Racing!!")

    imgcanvas = tkinter.Canvas(gamewindow, width=50, height=50, bg="red")
    imgcanvas.grid(row=0,column=0)
    img = ImageTk.PhotoImage(Image.open("goat.png"))    
    imgcanvas.create_image(20,20,image=img)

def generateEntries():
    global entrywindow
    entrywindow = Toplevel(window)
    entrywindow.geometry("2000x1000")
    entrywindow.title("Insert the player names")
    generateXandY()







window = tkinter.Tk()

numOfPlayers = Toplevel(window)
numOfPlayers.geometry("280x100")
numOfPlayers.title("How many players?")

howManyPlayersLabel = tkinter.Label(numOfPlayers,text="How many players are we playing with? (108 max)")
howManyPlayersLabel.grid(row=0,column=0)

entry = tkinter.Entry(numOfPlayers, width=20)
entry.grid(row=1,column=0)

nextbutton = tkinter.Button(numOfPlayers, text="Next", command=howManyPlayers)
nextbutton.grid(row=2,column=0)

numOfPlayers.lift(window)

window.mainloop()