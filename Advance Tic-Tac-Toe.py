import tkinter.messagebox
from tkinter import *

# #00BFFF -> Sky blue
# #008080 -> Teal blue-green
# #FDF200 -> Neon yellow
# #08FF08 -> Fluorescent green
# #6600FF -> Electric indigo
# #FFFD01 -> Bright yellow
# #39FF14 -> Neon green
# #FEFFFC -> White wash
# #11FF00 -> Phosphorescent green
root = Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toe")
root.configure(background="#00BFFF")

Tops = Frame(root, bg="#00BFFF", pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lblTitle = Label(Tops, font=('arial', 50, 'bold'), text="Advance Tic Tac Toe Game", bd=21, bg="#39FF14", fg="#6600FF", justify=CENTER)
lblTitle.grid(row=0, column=0)

MainFrame = Frame(root, bg="#FDF200", bd=10, width=1350, height=600, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg="#00BFFF", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=560, height=500, padx=10, pady=2, bg="#00BFFF", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg="#00BFFF", relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200, padx=10, pady=2, bg="#00BFFF", relief=RIDGE)
RightFrame2.grid(row=1, column=0)

PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)

buttons = StringVar()
click = True

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scoreKeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scoreKeeper()


def scoreKeeper():
    global tie

    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background="#11FF00")
        button2.configure(background="#11FF00")
        button3.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner", "X won the game")

    if(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        button4.configure(background="#11FF00")
        button5.configure(background="#11FF00")
        button6.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner", "X won the game")

    if(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        button7.configure(background="#11FF00")
        button8.configure(background="#11FF00")
        button9.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner", "X won the game")

    if(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        button3.configure(background="#11FF00")
        button5.configure(background="#11FF00")
        button7.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner", "X won the game")

    if(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        button1.configure(background="#11FF00")
        button5.configure(background="#11FF00")
        button9.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner", "X won the game")

    if(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        button1.configure(background="#11FF00")
        button4.configure(background="#11FF00")
        button7.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner", "X won the game")

    if(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        button2.configure(background="#11FF00")
        button5.configure(background="#11FF00")
        button8.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner", "X won the game")

    if(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        button3.configure(background="#11FF00")
        button6.configure(background="#11FF00")
        button9.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Winner", "X won the game")


    if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        button1.configure(background="#11FF00")
        button2.configure(background="#11FF00")
        button3.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner", "O won the game")

    if(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        button4.configure(background="#11FF00")
        button5.configure(background="#11FF00")
        button6.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner", "O won the game")

    if(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        button7.configure(background="#11FF00")
        button8.configure(background="#11FF00")
        button9.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner", "O won the game")

    if(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        button3.configure(background="#11FF00")
        button5.configure(background="#11FF00")
        button7.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner", "O won the game")

    if(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        button1.configure(background="#11FF00")
        button5.configure(background="#11FF00")
        button9.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner", "O won the game")

    if(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        button1.configure(background="#11FF00")
        button4.configure(background="#11FF00")
        button7.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner", "O won the game")

    if(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        button2.configure(background="#11FF00")
        button5.configure(background="#11FF00")
        button8.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner", "O won the game")

    if(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        button3.configure(background="#11FF00")
        button6.configure(background="#11FF00")
        button9.configure(background="#11FF00")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Winner", "O won the game")
    
    
    if(button1["text"]!=" " and button2["text"]!=" " and button3["text"]!=" " and button4["text"]!=" " and button5["text"]!=" " and button6["text"]!=" " and button7["text"]!=" " and button8["text"]!=" " and button9["text"]!=" "):
        tie = True
        tkinter.messagebox.showinfo("Tie", "It's a Tie")
        reset()
    


def reset():
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "

    button1.configure(background="#FFFD01")
    button2.configure(background="#FFFD01")
    button3.configure(background="#FFFD01")
    button4.configure(background="#FFFD01")
    button5.configure(background="#FFFD01")
    button6.configure(background="#FFFD01")
    button7.configure(background="#FFFD01")
    button8.configure(background="#FFFD01")
    button9.configure(background="#FFFD01")


def NewGame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)


lblPlayerX = Label(RightFrame1, font=('arial', 40, 'bold'), text="Player X: ", padx=2, pady=2, bg="#00BFFF")
lblPlayerX.grid(row=0, column=0, sticky=W)
txtPlayerX = Entry(RightFrame1, font=('arial', 40, 'bold'), bd=2, fg="#000000", textvariable=PlayerX, width=14, justify=LEFT).grid(row=0, column=1)

lblPlayerO = Label(RightFrame1, font=('arial', 40, 'bold'), text="Player O: ", padx=2, pady=2, bg="#00BFFF")
lblPlayerO.grid(row=1, column=0, sticky=W)
txtPlayerO = Entry(RightFrame1, font=('arial', 40, 'bold'), bd=2, fg="#000000", textvariable=PlayerO, width=14, justify=LEFT).grid(row=1, column=1)


btnReset = Button(RightFrame2, text="Reset", font=('arial 26 bold'), height=2, width=20, bg="#FEFFFC", command=reset)
btnReset.grid(row=2, column=0, padx=6, pady=11)

btnNewGame = Button(RightFrame2, text="New game", font=('arial 26 bold'), height=2, width=20, bg="#FEFFFC", command=NewGame)
btnNewGame.grid(row=3, column=0, pady=6, padx=10)


button1 = Button(LeftFrame, text=" ", font=('arial 26 bold'), height=3, width=8, bg="#FFFD01", command=lambda:checker(button1))
button1.grid(row=1, column=0, sticky = S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=('arial 26 bold'), height=3, width=8, bg="#FFFD01", command=lambda:checker(button2))
button2.grid(row=1, column=1, sticky = S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=('arial 26 bold'), height=3, width=8, bg="#FFFD01", command=lambda:checker(button3))
button3.grid(row=1, column=2, sticky = S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=('arial 26 bold'), height=3, width=8, bg="#FFFD01", command=lambda:checker(button4))
button4.grid(row=2, column=0, sticky = S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=('arial 26 bold'), height=3, width=8, bg="#FFFD01", command=lambda:checker(button5))
button5.grid(row=2, column=1, sticky = S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('arial 26 bold'), height=3, width=8, bg="#FFFD01", command=lambda:checker(button6))
button6.grid(row=2, column=2, sticky = S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=('arial 26 bold'), height=3, width=8, bg="#FFFD01", command=lambda:checker(button7))
button7.grid(row=3, column=0, sticky = S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=('arial 26 bold'), height=3, width=8, bg="#FFFD01", command=lambda:checker(button8))
button8.grid(row=3, column=1, sticky = S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=('arial 26 bold'), height=3, width=8, bg="#FFFD01", command=lambda:checker(button9))
button9.grid(row=3, column=2, sticky = S+N+E+W)

root.mainloop()