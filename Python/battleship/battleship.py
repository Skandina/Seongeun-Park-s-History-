from random import randint

board = [] 
board_in = [] 

for i in range(5):
    board.append(['O']*5)

def print_board(board_in):
    board_in = board[0:5]
    for s in board_in:
        print(*s)

def random_row(board_in):
    return randint(0,4)

def random_col(row_in):
    return randint(0,4)

ship_row = random_row(board)
ship_col = random_col(board)

print_board(board)

#board[ship_row][ship_col] = 'S'


n = 0
x = 1
while n<25:
    Guess_row = int(input("Guess row:"))-1
    Guess_col = int(input("Guess col:"))-1
    range_1 = range(0,5) 

    if  (Guess_row not in range_1) or (Guess_col not in range_1):
        print("That is not even in the ocean!")

    elif Guess_row == ship_row and Guess_col == ship_col:
         board[Guess_row][Guess_col] = 'S'
         print_board(board)
         print("Congratulations, you sank the ship!")
         break

    elif Guess_row != ship_row or Guess_col != ship_col: 
        board[Guess_row][Guess_col] = 'X'
        print_board(board)
        print("Sorry, you missed!" +str(x)+"/5")
        n +=1
        x +=1 

        if n == 5:
            print("Sorry, you lost")
            break