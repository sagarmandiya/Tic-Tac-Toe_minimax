#A board with either a human or a computer going first and 
#they can choose what to choose between zero or X.
#empty spaces would be hyphens(-), X's would be marked as 
#capital(X) and zero would be indicated as capital O.

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from functools import partial
from copy import deepcopy

global board
board = [[" " for x in range(3)] for y in range(3)]
window = tk.Tk()
#boardDesign()
def boardDesign():
    menu = Tk()
    menu.geometry("250x250")
    #menu.title("Tic Tac Toe Game")
    #withPC = partial(withpc, menu)
    #withPlayer = partial(withplayer, menu)
    
    head = Button(menu,text = "---Welcome to the game---",
                  activeforeground = 'red',
                  activebackground = "black", bg = "red",
                  fg = "black", width = 500, font = 'summer', bd = 5)
    
    B1 = Button(menu, text = "Single Player", activeforeground = 'red',
               activebackground = 'black', bg = "red", fg = "black",
               width = 500, font = 'summer', bd = 5)
    
    B2 = Button(menu, text = "Multi Player", #command = wpl,
                activeforeground = 'red',
                    activebackground = "black", bg = "red", fg = "black",
                    width = 500, font = 'summer', bd = 5)
         
    B3 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'red',
                activebackground = "black", bg = "red", fg = "black",
                width = 500, font = 'summer', bd = 5)
    head.pack(side = 'top')
    B1.pack(side = 'top')
    B2.pack(side = 'top')
    B3.pack(side = 'top')
    menu.mainloop()
    
if __name__ == '__main__':
    boardDesign()
    
