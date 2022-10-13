import tkinter as tk
from tkinter import *
from tkinter import messagebox
from functools import partial
from copy import deepcopy
import math
import os

class TicTacToe:

    # Attributes
    #moves - number of moves so far
    #board - string vector of length 9 ('-','X','O')
    #p1_sym - string denoting the symbol of the player that goes 1st
    #p2_sym - string denoting the symbol of the player that goes 2nd
    #p1_ctrl - string of 'AI' or 'HMN' to indicate who is controlling this player
    #p2_ctrl - string of 'AI' or 'HMN' to indicate who is controlling this player
    
    global board
    board = [[" " for x in range(3)] for y in range(3)]
    window = tk.Tk()
    
    
    def __init__(self):
        self.moves = 0
        self.board = [' '] * 9
        self.play()
    
    # ~~~ UI functions ~~~

    def drawBoard(self):
        menu = Tk()
        menu.geometry("250x250")
        menu.title("Tic Tac Toe Game")
        withPC = partial(withpc, menu)
        withPlayer = partial(withplayer, menu)
        
        head = Button(menu,text = "---Welcome to the game---",
                      activeforeground = 'red',
                      activebackground = "black", bg = "red",
                      fg = "black", width = 500, font = 'summer', bd = 5)
        
        B1 = Button(menu, text = "Single Player", activeforeground = 'red',command = withPC,
                   activebackground = 'black', bg = "red", fg = "black",
                   width = 500, font = 'summer', bd = 5)
        
        B2 = Button(menu, text = "Multi Player", command = withPlayer,
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
        # # prints a visual representation of the board
        # # Is run after every move
        # # Could clear console each time for a neat representation
        # board = self.board
        # print("\n")
        # print(" " + board[0] + " | "  + board[1] +  " | " + board[2])
        # print("---*---*---")
        # print(" " + board[3] + " | "  + board[4] +  " | " + board[5])
        # print("---*---*---")
        # print(" " + board[6] + " | "  + board[7] +  " | " + board[8])
        # print("\n")
    
    def gamePrompt(self):
        # Prompt to set self.p1_sym as 'X' or 'O' and self.p2_sym as the opposite
        self.p1_sym = 'X'
        self.p2_sym = 'O'
        # Prompt to set self.p1_ctrl as 'AI' or 'HMN'
        self.p1_ctrl = 'HMN'
        # Prompt to set self.p2_ctrl as 'AI' or 'HMN'
        self.p2_ctrl = 'HMN'
        return

    def movePrompt(self):

        # A move is an integer of position (0-8)

        while True:
            
            # Prompt player for a move (change existing 'move' variable)
            move = int(input("Enter the position [0-8]: ")) 

            # Check first so that only valid moves will be returned by this function
            if self.isValidMove(move):
                return move


    def getMove(self):
        if (self.moves % 2) == 0:
            # Player2's turn
            if self.p2_ctrl == 'HMN':
                return self.movePrompt()
            else:
                return self.findBestMove()
        else:
            # Player1's turn
            if self.p1_ctrl == 'HMN':
                return self.movePrompt()
            else:
                return self.findBestMove()
    
    def isValidMove(self, move):
        # Accept Input func
        # 1. Validate the move
        # 2a. Output the move if valid
        # 2b. If invalid, output ??
        board = self.board
        if board[move] == " ":
            return True
        else:
            print("Invalid Move! Please try again. ")
            return False

    def makeMove(self, move):
        if (self.moves % 2) == 0:
            # Player2's turn; use self.p2_sym for the appropriate symbol
            curr_sym = self.p2_sym
        else:
            # Player1's turn; use self.p1_sym for the appropriate symbol
            curr_sym = self.p1_sym
        
        board = self.board
        board[move] = curr_sym

    def printOutput(self, result):
        # Print the result of the game
        if(result == "Cats"):
            print("\nDraw!\n")
        else:
            print("\n" + str(result) + " Won!\n")
        return

    def playAgainPrompt(self):
        # Prompt player to play again. If no, then print exit message. If yes, then run self.play()
        return

    # ~~~ Minimax functions ~~~

    def findBestMove(self):
        # Returns the best move
        best_score = -math.inf
        best_move = 0
        board = self.board

        if (self.moves % 2) == 0:
            # Player2's turn; use self.p2_sym for the appropriate symbol
            curr_sym = self.p2_sym
        else:
            # Player1's turn; use self.p1_sym for the appropriate symbol
            curr_sym = self.p1_sym

        for pos in range(len(board)):
            if board[pos] == " ":
                board[pos] = curr_sym
                score = self.minimax(False)
                # resetting the position
                board[pos] = " "

                if score > best_score:
                    best_score = score
                    best_move = pos 
        
        self.makeMove(best_move)
        return

    def max(self):
        # insert func
        return

    def min(self):
        # insert func
        return

    # ~~~ Game Logic functions ~~~

    def check_game_over(self):

        # Output is 'X', 'O', or 'Cats' (for tie)
        # Empty output ("") if game is not yet over

        # Winning combinations:
        # Horizontal: (0,1,2), (3,4,5), (6,7,8)
        # Vertical: (0,3,6), (1,4,7), (2,5,8)
        # Diagonal: (0,4,8), (2,4,6)

        # Horizontal Wins
        if (self.board[0] == self.board[1] == self.board[2] and self.board[0] != ' '):
            return self.board[0]
        elif (self.board[3] == self.board[4] == self.board[5] and self.board[3] != ' '):
            return self.board[3]
        elif (self.board[6] == self.board[7] == self.board[8] and self.board[6] != ' '):
            return self.board[6]

        # Vertical Wins
        if (self.board[0] == self.board[3] == self.board[6] and self.board[0] != ' '):
            return self.board[0]
        elif (self.board[1] == self.board[4] == self.board[7] and self.board[1] != ' '):
            return self.board[1]
        elif (self.board[2] == self.board[5] == self.board[8] and self.board[2] != ' '):
            return self.board[2]

        # Diagonal Wins
        if (self.board[0] == self.board[4] == self.board[8] and self.board[0] != ' '):
            return self.board[0]
        elif (self.board[2] == self.board[4] == self.board[6] and self.board[2] != ' '):
            return self.board[2]

        # No free squares left
        if ' ' not in self.board:
            return "Cats"
        # No end condition met (game not over yet)
        else:
            return ""
        
        
    # Controlling function for game logic
    def play(self):
        self.gamePrompt()
        while True:
            
            os.system("clear")
            self.drawBoard()
            result = self.check_game_over()
            if result != "":
                #self.printOutput(result)
                self.playAgainPrompt()
                break
            else:
                self.moves += 1
    
            self.makeMove(self.getMove())
            
        
# Configure text on button while playing with another player
def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 1 won the match")
    elif winner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 2 won the match")
    elif(isfull()):
        gb.destroy()
        box = messagebox.showinfo("Tie Game", "Tie Game")



# Configure text on button while playing with system
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
    elif(isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
    if(x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)
 


#Create the GUI of game board for play along with system
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Create the GUI of game board for play along with another player
def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
    
    
# Initialize the game board to play with system
def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text = "Computer : O",
                width = 10, state = DISABLED)
     
    l2.grid(row = 2, column = 1)
    gameboard_pc(game_board, l1, l2)
     
        
     
# Initialize the game board to play with another player
def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text = "Player 1 : X", width = 10)
     
    l1.grid(row = 1, column = 1)
    l2 = Button(game_board, text = "Player 2 : O",
                width = 10, state = DISABLED)
     
    l2.grid(row = 2, column = 1)
    gameboard_pl(game_board, l1, l2)
        
            

def main():
    ttt = TicTacToe()
    ttt.play()

if __name__ == "__main__":
    main()
