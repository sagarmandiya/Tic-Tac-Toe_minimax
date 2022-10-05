class TicTacToe:

    # Attributes
    #Moves - number of moves so far
    #Player1 - goes 1st
    #Player2 - goes 2nd
    #Board - string vector of length 9 ('-','X','O')
    #[Move is a vector of position (0-8) and symbol ('X','O')]
    

    def __init__(self):
        self.moves = 0
        self.board = ['-'] * 9
        self.play()


    # ~~~ UI / Game progression functions ~~~

    def drawBoard(self):
        # prints a visual representation of the board
        # Is run after every move
        # Could clear console each time for a neat representation
        return
    
    def gamePrompt(self):
        # Needs to set self.Player1 and self.Player2 as 'X' or 'O'
        return

    def isValidMove(self, move):
        # Accept Input func
        # 1. Validate the move
        # 2a. Output the move if valid
        # 2b. If invalid, output ??
        return

    def playAgainPrompt(self):
        # Prompt player to play again. If no, then print exit message. If yes, then run self.play()
        return

    def printOutput(result):
        # Print the result of the game
        return

    # ~~~ Minimax functions ~~~

    def findBestMove(self):
        # Uses max and min functions recursively
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

            if (self.moves % 2) == 0:
                # Player2's turn
                break
            else:
                # Player1's turn
                break
            return
        return
            
            

def main():
    ttt = TicTacToe()
    ttt.play()

if __name__ == "__main__":
    main()