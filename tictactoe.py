import sys
from IPython.display import clear_output
from random import randint
def print_board(board):
    print(" "+board[6]+" | "+board[7]+" | "+board[8]+" ")
    print("-----------")
    print(" "+board[3]+" | "+board[4]+" | "+board[5]+" ")
    print("-----------")
    print(" "+board[0]+" | "+board[1]+" | "+board[2]+" ")
def user_input(board,chance):
    value=int(input('Enter position (1-9)'))
    while 1:
        if value>=1 and value<=9:
            if board[value-1]==' ':
                if chance:
                    board[value-1]='X'
                else:
                    board[value-1]='O'
                break
            else:
                print('Invalid Position')
        else:
            print('Invalid Position')
        value=int(input('Enter position (1-9)'))
def check_winner(board,lastchance):
    checkfor=''
    if lastchance:
        checkfor='X'
    else:
        checkfor='O'
    if board[0]==checkfor and board[1]==checkfor and board[2]==checkfor:
        return 1
    elif board[3]==checkfor and board[4]==checkfor and board[5]==checkfor:
        return 1
    elif board[6]==checkfor and board[7]==checkfor and board[8]==checkfor:
        return 1
    elif board[0]==checkfor and board[3]==checkfor and board[6]==checkfor:
        return 1
    elif board[1]==checkfor and board[4]==checkfor and board[7]==checkfor:
        return 1
    elif board[2]==checkfor and board[5]==checkfor and board[8]==checkfor:
        return 1
    elif board[2]==checkfor and board[4]==checkfor and board[6]==checkfor:
        return 1
    elif board[0]==checkfor and board[4]==checkfor and board[8]==checkfor:
        return 1
    else:
        return 0
def play_game(board):
    toss=randint(0,1)
    if toss==0:
        print('Player 1 will go first')
    else:
        print('Player 2 will go first')
    choice=''
    print(f'Player {toss+1} choose your token ( X or O )',end=' ')
    while choice not in ['X','O']:
        choice=input('->')
    chance=None
    if choice=='X':
        chance=True
    else:
        chance=False
    while 1:
        clear_output()
        print_board(board)
        print(f'Player {toss+1} choose your position->')
        user_input(board,chance)
        ans=check_winner(board,chance)
        if ans:
            clear_output()
            print_board(board)
            print(f'Player {toss+1} won. Congratulations !')
            break
        else:
            if ' ' not in board:
                clear_output()
                print_board(board)
                print('Its a Draw !')
                break
        if toss==0:
            toss=1
        else:
            toss=0
        chance=not chance
    response=''
    while response not in ['Yes','No']:
        response=input('Do you wish to play again ?')
    if response=='Yes':
        board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
        play_game(board)
    else:
        return
print('Welcome to TIC TAC TOE')
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
play=input('Do you want to start playing or exit the game ? (Play/ExitGame)')
while play not in ['Play','ExitGame']:
    play=input('Do you want to start playing or exit the game ? (Play/ExitGame)')
if play=='Play':
    play_game(board)
