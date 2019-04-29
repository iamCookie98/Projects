def print_board(board): 
    for row in board:
        print (" ".join(row))
def random_row(board):
    return randint(0, len(board) - 1)
def random_col(board):
    return randint(0, len(board[0]) -1)
    
from random import randint
board = []
for x in range(1, 11):
        board.append(["O"] * 10)
        
print_board(board)
ship1 = (random_row(board), random_col(board))
ship2 = (random_row(board), random_col(board))#, ship2[0] + 1, ship2[1] + 1)
print (ship1, "ship1")
print (ship2, "ship2")
shipleft = [ship1, ship2]
print (shipleft)

#while len(shipleft) != 0:
for turn in range(4):
    while len(shipleft) != 0:
        print("Turn", (turn + 1))
        guess_row = int(input("Guess Row: ")) - 1
        guess_col = int(input("Guess Col: ")) - 1

        #while len(shipleft) != 0:
        #if ship1 == (guess_row, guess_col ) or ship2 == (guess_row + 1, guess_col + 1):
        if ship1 == (guess_row, guess_col) or ship2 == (guess_row, guess_col):
            board[guess_col][guess_row] = "H"
            print ("Congratulations! You hit my battleship!")
            shipleft.remove((guess_row, guess_col))
            print_board(board)
            print ((guess_row, guess_col), "guess row, guess col")
            print (len(shipleft), "shipleft")
            print ("  ")
            if len(shipleft) == 0:
                print('You won')
            #continue
        else:
            if guess_row not in range(11) or guess_col not in range(11):
                print ("That is not even in the map.")
            elif board[guess_col][guess_row] == "X":
                 print( "You guessed that one already." )
            else:
                print ("You missed my battleship!")
                board[guess_col][guess_row] = "X"
                print ((guess_row, guess_col), "guess row, guess col")
                print (len(shipleft), "shipleft")
                print ("  ")
            if (turn == 3):
                print ("Game Over")
                print_board(board)
                break
            print_board(board)
        break