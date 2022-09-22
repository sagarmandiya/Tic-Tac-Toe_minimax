Class TicTacToe

    Moves - number of moves so far
    Player1 - goes 1st
    Player2 - goes 2nd
    Board - string vector of length 9 ('-','X','O')
    [Move is a vector of position (0-8) and symbol ('X','O')]
    
    Initializer
        Player1 picks X or O? (or is this in play game)

    def __init__(self):
        self.moves = 0
        self.board = ['-'] * 9
        self.play()


    Draw board function


    Accept Input
    - validate move
    -> Output

    Find best move
    - Uses max and min functions recursively

    Max function

    Min function

    Play again prompt function

    def check_game_over(self):

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
        
        Output is 'X', 'O', or 'Cats'
        

    def play(self):
        while True:
            
            Draw board function
            if self.check_game_over() != "":
                Output Result function(self.check_game_over())
                Play again prompt function
                break
            else:
                self.moves++

            if (moves % 2) == 0:
                Player2's turn
            else:
                Player1's turn
            
            


Main
- calls game class to play
