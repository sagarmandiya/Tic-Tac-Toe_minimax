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
        self.board = ['-'] * 9
        self.play()


    # ~~~ UI functions ~~~

    def drawBoard(self):
        # prints a visual representation of the board
        # Is run after every move
        # Could clear console each time for a neat representation
        return
    
    def gamePrompt(self):
        # Prompt to set self.p1_sym as 'X' or 'O' and self.p2_sym as the opposite
        # Prompt to set self.p1_ctrl as 'AI' or 'HMN'
        # Prompt to set self.p2_ctrl as 'AI' or 'HMN'
        return

    def movePrompt(self):
        
        if (self.moves % 2) == 0:
            # Player2's turn; use self.p2_sym for the appropriate symbol
            curr_sym = self.p2_sym
        else:
            # Player1's turn; use self.p1_sym for the appropriate symbol
            curr_sym = self.p1_sym

        # A move is a vector of position (0-8) and symbol ('X','O')
        # Set a default, invalid move to begin with
        move = [-1, curr_sym]

        while True:
            
            # Check first so that only valid moves will be returned by this function
            if self.isValidMove(move != ""):
                return move
            else:
                # Prompt player for a move (change existing 'move' variable)
                move


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
        return

    def printOutput(result):
        # Print the result of the game
        return

    def playAgainPrompt(self):
        # Prompt player to play again. If no, then print exit message. If yes, then run self.play()
        return

    # ~~~ Minimax functions ~~~

    def findBestMove(self):
        # Uses max and min functions recursively
        # Returns the best move
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
        if self.board[0] == self.board[1] == self.board[2]:
            return self.board[0]
        elif self.board[3] == self.board[4] == self.board[5]:
            return self.board[3]
        elif self.board[6] == self.board[7] == self.board[8]:
            return self.board[6]

        # Vertical Wins
        if self.board[0] == self.board[3] == self.board[6]:
            return self.board[0]
        elif self.board[1] == self.board[4] == self.board[7]:
            return self.board[1]
        elif self.board[2] == self.board[5] == self.board[8]:
            return self.board[2]

        # Diagonal Wins
        if self.board[0] == self.board[4] == self.board[8]:
            return self.board[0]
        elif self.board[2] == self.board[4] == self.board[6]:
            return self.board[2]

        # No free squares left
        if '-' not in self.board:
            return "Cats"
        # No end condition met (game not over yet)
        else:
            return ""
        
        
    # Controlling function for game logic
    def play(self):
        while True:
            
            self.drawBoard()
            result = self.check_game_over()
            if result != "":
                self.printOutput(result)
                self.playAgainPrompt()
                break
            else:
                self.moves += 1

            self.getMove()
            
            

def main():
    ttt = TicTacToe()
    ttt.play()

if __name__ == "__main__":
    main()