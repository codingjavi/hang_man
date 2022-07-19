class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = none

    def print_board(self):    #this is a row (tells us indices like 1,2,3 is first row and 4,5,6 is second)
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]: #getting rows
            print ('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        #tells us what numbers corresponds to what box
        number_board = [[str(i) for range(j*3, (j+1)*3)] for j in range (3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            