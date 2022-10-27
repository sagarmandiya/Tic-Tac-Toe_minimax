# TIC-TAC-TOE
# Contributions by Sagar Mandiya, Shubham Mishra, Aaron B
# ROLES: Written by Sagar
#        Organised by AAron
#        UI by Shubham


import math
import os


def drawBoard(board):
    # prints a visual representation of the board
    # Is run after every move
    # Could clear console each time for a neat representation
    print("\n")
    print(" " + board[0] + " | "  + board[1] +  " | " + board[2])
    print("---*---*---")
    print(" " + board[3] + " | "  + board[4] +  " | " + board[5])
    print("---*---*---")
    print(" " + board[6] + " | "  + board[7] +  " | " + board[8])
    print("\n")


def isValidMove(board, position):
    if position >= 0 and position <= 8:
        if board[position] == " ":
            return True
        else:
            return False
    else:
        return False


def makeMove(board, position, player_char, player):
    if isValidMove(board, position) == True:
        board[position] = player_char
        os.system("clear")
        drawBoard(board)

        if check_game_over(board) == 1:
            print("\nDraw!\n")
        
        elif check_game_over(board) == 2:
            print("\n" + str(player) + " Won!\n")
        
        return

    else:
        print("Invalid Move! Please try again. ")
        position = int(input("Enter new position: ")) 
        makeMove(board, position, player_char, player)
        return


def check_game_over(board):

    # Output is 'X', 'O', or 'Cats' (for tie)
    # Empty output ("") if game is not yet over

    # Winning combinations:
    # Horizontal: (0,1,2), (3,4,5), (6,7,8)
    # Vertical: (0,3,6), (1,4,7), (2,5,8)
    # Diagonal: (0,4,8), (2,4,6)

    # Horizontal Wins
    if board[0] == board[1] == board[2] != " ":
        # return self.board[0]
        return 2
    elif board[3] == board[4] == board[5] != " ":
        # return self.board[3]
        return 2
    elif board[6] == board[7] == board[8] != " ":
        # return self.board[6]
        return 2

    # Vertical Wins
    if board[0] == board[3] == board[6] != " ":
        # return self.board[0]
        return 2
    elif board[1] == board[4] == board[7] != " ":
        # return self.board[1]
        return 2
    elif board[2] == board[5] == board[8] != " ":
        # return self.board[2]
        return 2

    # Diagonal Wins
    if board[0] == board[4] == board[8] != " ":
        # return self.board[0]
        return 2
    elif board[2] == board[4] == board[6] != " ":
        # return self.board[2]
        return 2

    # No free squares left
    if ' ' not in board:
        # return "Cats"
        return 1
    # No end condition met (game not over yet)
    else:
        return 0

def check_player_won(board, player_char):

    # Horizontal Wins
    if board[0] == board[1] == board[2] == player_char:
        # return self.board[0]
        return 2
    elif board[3] == board[4] == board[5] == player_char:
        # return self.board[3]
        return 2
    elif board[6] == board[7] == board[8] == player_char:
        # return self.board[6]
        return 2

    # Vertical Wins
    if board[0] == board[3] == board[6] == player_char:
        # return self.board[0]
        return 2
    elif board[1] == board[4] == board[7] == player_char:
        # return self.board[1]
        return 2
    elif board[2] == board[5] == board[8] == player_char:
        # return self.board[2]
        return 2

    # Diagonal Wins
    if board[0] == board[4] == board[8] == player_char:
        # return self.board[0]
        return 2
    elif board[2] == board[4] == board[6] == player_char:
        # return self.board[2]
        return 2

    # No free squares left
    if " " not in board:
        # return "Cats"
        return 1
    # No end condition met (game not over yet)
    else:
        return 0

# Takes the input and makes the move. 
def player_move(board, player_char, player):
    position = int(input("Enter the position: ")) 
    position = position - 1
    makeMove(board, position=position, player_char=player_char, player=player)

# function for bot move when the game type is set to pvc
def bot_move(board, player_char, player, game_type):
    if game_type == "pvp":
        position = int(input("Enter the position: "))
        makeMove(board, position=position, player_char=player_char, player=player)
    else:
        best_score = -math.inf
        best_move = 0

        for pos in range(len(board)):
            if board[pos] == " ":
                board[pos] = player_char
                score = minimax(board, player_char, False)
                # resetting the position
                board[pos] = " "

                if score > best_score:
                    best_score = score
                    best_move = pos 
        
        makeMove(board, best_move, player_char, player)
        return

# Minimax function to 
def minimax(board, player_char, maximize):
    # opponent = "X" if player_char == "O" else "O"

    if check_player_won(board, "O") == 2:
        return 1

    elif check_player_won(board, "X") == 2:
        return -1

    elif check_game_over(board) == 1:
        return 0

    if maximize:
        best_score = -math.inf

        for pos in range(len(board)):
            if board[pos] == " ":
                board[pos] = "O"
                score = minimax(board, "O", False)
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
                board[pos] = "X"
                score = minimax(board, "X", True)
                # print("$\n")
                # drawBoard(board)

                # resetting the position
                board[pos] = " "

                if score < best_score:
                    best_score = score
        
        return best_score


board = [" "] * 9

human = "X"
bot = "O"
game_type = "pvc"

first_player = human

print("\n************* TIC-TAC-TOE *************\n\nWelcome!\n") 
print("You are playing today as {}\n".format(human))
print("Enter the position of the board ranging from 1 - 9, going horizontally.\n")

drawBoard(board=board)

while (check_game_over(board) == 0):
    if first_player == human:
        if check_game_over(board) == 0:
            player_move(board, player_char=human, player="You")

        if check_game_over(board) == 0:
            bot_move(board, player_char=bot, player="Bot", game_type=game_type)
    
    else:
        if check_game_over(board) == 0:
            bot_move(board, player_char=bot, player="Bot", game_type=game_type)

        if check_game_over(board) == 0:
            player_move(board, player_char=human, player="You")
