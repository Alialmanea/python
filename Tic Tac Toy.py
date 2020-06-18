from tkinter import *
from tkinter import ttk


def buClick(bu_number):
    global ActivePlayer

    if ActivePlayer == 1:
        player_1.append(bu_number)
        root.title("Tic Tac Toy : Player 2")
        setLayout(bu_number, 'X')
        ActivePlayer = 2
        #print("player_1 : {} ".format(player_1))

    else:
        player_2.append(bu_number)
        root.title("Tic Tac Toy : Player 1")
        setLayout(bu_number, 'o')
        ActivePlayer = 1
        #print("player_2 : {}".format(player_2))

    checkWinner()

    if Winner == 1:
        print("player 1 is the winner")
        root.title("Player 1 is The Winner")
        for w in root.winfo_children():
            w.configure(state="disabled")
    if Winner == 2:
        print("player 2 is the winner")
        root.title("Player 2 is The Winner")
        for w in root.winfo_children():
            w.configure(state="disabled")
    if Winner ==-1 and (len(player_1) == 5 and  len(player_2) == 4):  
        root.title(" Tie ")
        for w in root.winfo_children():
            w.configure(state="disabled")

def setLayout (bu_number, text):

    if bu_number == 1:
        Button_1.config(text=text)
        Button_1.state(['disabled'])
    if bu_number == 2:
        Button_2.config(text=text)
        Button_2.state(['disabled'])
    if bu_number == 3:
        Button_3.config(text=text)
        Button_3.state(['disabled'])
    if bu_number == 4:
        Button_4.config(text=text)
        Button_4.state(['disabled'])
    if bu_number == 5:
        Button_5.config(text=text)
        Button_5.state(['disabled'])
    if bu_number == 6:
        Button_6.config(text=text)
        Button_6.state(['disabled'])
    if bu_number == 7:
        Button_7.config(text=text)
        Button_7.state(['disabled'])
    if bu_number == 8:
        Button_8.config(text=text)
        Button_8.state(['disabled'])
    if bu_number == 9:
        Button_9.config(text=text)
        Button_9.state(['disabled'])

def  checkWinner():
    global Winner
#For Player 1
    if 1 in player_1 and 2 in player_1 and 3 in player_1:
        Winner = 1
    if 4 in player_1 and 5 in player_1 and 6 in player_1:
        Winner = 1
    if 7 in player_1 and 8 in player_1 and 9 in player_1:
        Winner = 1

    if 1 in player_1 and 4 in player_1 and 7 in player_1:
        Winner = 1
    if 2 in player_1 and 5 in player_1 and 8 in player_1:
        Winner = 1
    if 3 in player_1 and 6 in player_1 and 9 in player_1:
        Winner = 1

    if 1 in player_1 and 5 in player_1 and 9 in player_1:
        Winner = 1
    if 3 in player_1 and 5 in player_1 and 7 in player_1:
        Winner = 1

# For Player 2
    if 1 in player_2 and 2 in player_2 and 3 in player_2:
        Winner = 2
    if 4 in player_2 and 5 in player_2 and 6 in player_2:
        Winner = 2
    if 7 in player_2 and 8 in player_2 and 9 in player_2:
        Winner = 2

    if 1 in player_2 and 4 in player_2 and 7 in player_2:
        Winner = 2
    if 2 in player_2 and 5 in player_2 and 8 in player_2:
        Winner = 2
    if 3 in player_2 and 6 in player_2 and 9 in player_2:
        Winner = 2

    if 1 in player_2 and 5 in player_2 and 9 in player_2:
        Winner = 2
    if 3 in player_2 and 5 in player_2 and 7 in player_2:
        Winner = 2


player_1 = []
player_2 = []
ActivePlayer = 1
Winner = -1


root=Tk()
root.title('Tic Toc Toy Player 1')
style = ttk.Style()
style.theme_use('classic')






Button_1 = ttk.Button(root, text='')
Button_1.grid(row=0, column=0, sticky='snew', ipadx=40, ipady=40)
Button_1.config(command=lambda :buClick(1))



Button_2 = ttk.Button(root, text='')
Button_2.grid(row=0, column=1, sticky='snew', ipadx=40, ipady=40)
Button_2.config(command=lambda :buClick(2))

Button_3 = ttk.Button(root, text='')
Button_3.grid(row=0, column=2, sticky='snew', ipadx=40, ipady=40)
Button_3.config(command=lambda :buClick(3))

Button_4 = ttk.Button(root, text='')
Button_4.grid(row=1, column=0, sticky='snew', ipadx=40, ipady=40)
Button_4.config(command=lambda :buClick(4))

Button_5 = ttk.Button(root, text='')
Button_5.grid(row=1, column=1, sticky='snew', ipadx=40, ipady=40)
Button_5.config(command=lambda :buClick(5))

Button_6 = ttk.Button(root, text='')
Button_6.grid(row=1, column=2, sticky='snew', ipadx=40, ipady=40)
Button_6.config(command=lambda :buClick(6))

Button_7 = ttk.Button(root, text='')
Button_7.grid(row=2, column=0, sticky='snew', ipadx=40, ipady=40)
Button_7.config(command=lambda :buClick(7))

Button_8 = ttk.Button(root, text='')
Button_8.grid(row=2, column=1, sticky='snew', ipadx=40, ipady=40)
Button_8.config(command=lambda :buClick(8))

Button_9 = ttk.Button(root, text='')
Button_9.grid(row=2, column=2, sticky='snew', ipadx=40, ipady=40)
Button_9.config(command=lambda :buClick(9))

root.mainloop()
