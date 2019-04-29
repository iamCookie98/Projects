from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print (" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
    print (" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
    print (" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    
def player_input():
    player1 = ''
    while player1.lower() != 'x' and player1.lower() != 'o':
        player1 = input("Please select marker X or O")
        
    if player1.lower() == 'x':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'
    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker
    
def win_check(board, mark):
    #if board[1:4] or board[4:7] or board[7:10] or board[7:10]
    return (board[1] == board[2] == board[3] == mark) or (board[4] == board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or (board[1] == board[5] == board[9] == mark) or (board[7] == board[5] == board[3] == mark) 

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    
def space_check(board, position):
    return board[position] == ''
    
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Choose your position from 1-9'))
        
    return position
    
def replay():
    replay = input("Do you want to play again? Yes or No")
    while():
        if replay.lower() == 'y' or replay.lower() == 'yes':
            return True
        elif replay.lower() == 'n' or replay.lower() == 'no':
            return False
        else:
        	print ("Enter again")
        	replay
            
while True:
    # Play the game up here
    the_boardinput = ['']*10
    player1, player2 = player_input()
    
    turn = choose_first()
    print (turn + 'will go first')
    
    play = input('Ready? y or n?')
    if play == 'y':
        play = True
    else:
        play = False
    
    #Game Started
    while play:
        #Player 1 Turn
        if turn == 'Player 1':
            #print ("Player 1 turn")
            display_board(the_boardinput)  #show the board display
            print ("Player 1 turn")
            
        #Choose a position
            position = player_choice(the_boardinput)
        
        #Place marker
            place_marker(the_boardinput, player1, position)
        
        #Check if they won
            if win_check(the_boardinput, player1):
                display_board(the_boardinput)
                print('PLAYER 1 HAS WON')
                play = False
                
        #Check if there is a tie
            else:
                if full_board_check(the_boardinput):
                    display_board(the_boardinput)
                    print("TIE GAME!")
                    play = False
                else:
                    turn = 'Player 2'
    
    
        # Player2's turn.
        else:
            display_board(the_boardinput)  #show the board display
            print ('Player 2 turn')
            
        #Choose a position
            position = player_choice(the_boardinput)
        
        #Place marker
            place_marker(the_boardinput, player2, position)
        
        #Check if they won
            if win_check(the_boardinput, player2):
                display_board(the_boardinput)
                print('PLAYER 2 HAS WON')
                play = False
                
        #Check if there is a tie
            else:
                if full_board_check(the_boardinput):
                    display_board(the_boardinput)
                    print("TIE GAME!")
                    play = False
                else:
                    turn = 'Player 1'

    if not replay():
        break
        #break out of while loop on replay