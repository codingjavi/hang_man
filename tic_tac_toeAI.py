import random
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

#main function that runs the game and encompases all the other functions
def play_game():
    display_board()
    
    #while game_still_going is True it'll keep running
    while game_still_going:

        #makes the player make a turn
        handle_turn(current_player)

        #if X wins the game will be over and the computer won't go
        check_if_gameover()
        if game_still_going == False:
            break
        computer_plays()
        #checks if the game is over
        check_if_gameover()


    #out of loop end of game
    if winner == "X" or winner == "O":
        print (winner + " won")
    elif winner == None:
        print ("Tie")


def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    
    #to check if the users input is valid, if valid is True it will continue
    valid = False
    while not valid:

        # check if number is in the range, loop in a loop
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            #takes us back here if the position isn't open
            position = input("Choose a position from 1-9 please: ")
 
        # Get correct index in our board list
        position = int(position) - 1

        # Then check if that spot is open
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    #changes the board[position] to the player(which is X or O)
    board[position] = player

    display_board()

#computer makes move
def computer_plays():
    
    #making sure the computer chooses a valid number and space
    valid = False

    #while not false it will continue
    while not valid:
        #I chose range (1, 9) because it kept choosing 10 in range(1,10)
        computer = random.choice(range(1,9))
        if board[computer] == "-":
            valid = True
        

    board[computer] = "O"
    print ("---------")
    
    display_board()
#game is over if there is a win or tie
def check_if_gameover():
    
    #check is there's a win first incase all the "-" are gone
    check_if_win()
    check_if_tie()


def check_if_win():
    #have to make winner a global to be able to access it in this function
    global winner

    #checks the check_rows() fucntion and if it returns something row_winner is a declared variable 
    row_winner = check_rows()

    column_winner = check_columns()

    diagnal_winner = check_diagnals()
    
    #if row_winner is a variable then winner equals row_winner which is X or Y
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagnal_winner:
        winner = diagnal_winner
    else:
        winner = None
    
    

#checks if theres a win in rows
def check_rows():

    #need these variables in this function so making them global
    global winner
    global game_still_going

    #if board[0-2] are the same(Xs or Os) and not equal to "-" then row_1 is created 
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    
    #if row_1 through 3 are created then game_still_going is False and the while loop stop
    if row_1 or row_2 or row_3:
        game_still_going = False

    #checks to see who was winner, it returns X or Y which is set to the variable row_winner 
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    
 
#same thing as rows
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
    
    
#checks diangnals for wins
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
    

#if there is no win and there's no more "-" then it is a tie
def check_if_tie():
    global game_still_going
    if "-" not in board:
        #set to false to end while loop
        game_still_going = False
    
    
#player flips after every turn
def flip_player():
    global current_player
    #if the player is X switch it to O
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    

#runs the game
play_game()