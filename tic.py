#Creating Global Variable
from logging.config import valid_ident


game_still_going = True
winner = None
current_player = "X"

#making the board
board = ["-","-","-","-","-","-","-","-","-"]

#displaying the board
def display_board():
    print (board[0] + " | " + board[1] + " | " + board[2])
    print (board[3] + " | " + board[4] + " | " + board[5])
    print (board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    display_board()

    while game_still_going:


        handle_turn(current_player)

        check_if_gameover()

        flip_player()

    #end of game
    if winner == "X" or winner == "O":
        print (winner + " won")
    elif winner == None:
        print ("Tie")

def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    
    valid = False
    while not valid:

        # check if number is in the range
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
 
        # Get correct index in our board list
        position = int(position) - 1

        # Then check if that spot is open
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = player

    display_board()

def check_if_gameover():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    row_winner = check_rows()

    column_winner = check_columns()

    diagnal_winner = check_diagnals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagnal_winner:
        winner = diagnal_winner
    else:
        winner = None
    
    return

def check_rows():
    global winner
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global winner
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return
    

def check_diagnals():
    global winner
    global game_still_going
    diagnal_1 = board[0] == board[4] == board[8] != "-"
    diagnal_2 = board[2] == board[4] == board[6] != "-"
    if diagnal_1 or diagnal_2:
        game_still_going = False

    if diagnal_1:
        return board[0]
    elif diagnal_2:
        return board[1]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return
    

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

play_game()
