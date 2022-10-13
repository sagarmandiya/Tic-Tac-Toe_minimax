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
    
    
    def __init__(self):
        self.moves = 0
        self.board = [' '] * 9
        self.play()


    # ~~~ UI functions ~~~

    def drawBoard(self):
        # prints a visual representation of the board
        # Is run after every move
        # Could clear console each time for a neat representation
        board = self.board
        print("\n")
        print(" " + board[0] + " | "  + board[1] +  " | " + board[2])
        print("---*---*---")
        print(" " + board[3] + " | "  + board[4] +  " | " + board[5])
        print("---*---*---")
        print(" " + board[6] + " | "  + board[7] +  " | " + board[8])
        print("\n")
    
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
        

    def minimax(self, maximize):
        board = self.board
        # opponent = "X" if player_char == "O" else "O"


        if (self.moves % 2) == 0:
            # Player2's turn; use self.p2_sym for the appropriate symbol
            curr_sym = self.p2_sym
        else:
            # Player1's turn; use self.p1_sym for the appropriate symbol
            curr_sym = self.p1_sym

        if (curr_sym == 'X'):
            next_sym = 'O'
        else:
            next_sym = 'X'

        if self.check_game_over() == curr_sym:
            return 1
        elif self.check_game_over() == next_sym:
            return -1
        elif self.check_game_over() == "Cats":
            return 0

        if maximize:
            best_score = -math.inf

            for pos in range(len(board)):
                if board[pos] == " ":
                    board[pos] = curr_sym
                    score = self.minimax(False)
                    # print("*\n")
                    # drawBoard(board)

                    # resetting the position
                    board[pos] = " "

                    if score > best_score:
                        best_score = score
            
            return best_score
        
        else:
            best_score = math.inf

            for pos in range(len(board)):
                if board[pos] == " ":
                    board[pos] = next_sym
                    score = self.minimax(True)
                    # print("$\n")
                    # drawBoard(board)

                    # resetting the position
                    board[pos] = " "

                    if score < best_score:
                        best_score = score
            
            return best_score

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
                self.printOutput(result)
                self.playAgainPrompt()
                break
            else:
                self.moves += 1

            self.makeMove(self.getMove())
            
            

def main():
    ttt = TicTacToe()
    ttt.play()

if __name__ == "__main__":
    main()