import random
board=["-","-","-","-","-","-","-","-","-"]
cp="X"
winner=None
gr=True
def printBoard(board):
    print(board[0]+board[1]+board[2])
    print("------")
    print(board[3]+board[4]+board[5])
    print("------")
    print(board[6]+board[7]+board[8])
def player(board):
    p=int(input("Select a spot b/w 1-9"))
    if board[p-1]=="-":
        board[p-1]=cp
    else:
        print("oops already a player is in that spot")
        player(board)
def ch(board):
    if board[0]==board[1]==board[2] and board[0]!="-":
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[8]!="-":
        winner=board[7]
        return True
def cv(board):
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[7]!="-":
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[8]!="-":
        winner=board[8]
        return True
def cd(board):
    if board[0]==board[4]==board[8] and board[0]!="-":
        winner=board[0]
        return True
    elif board[2]==board[4]==board[6] and board[6]!="-":
        winner=board[1]
        return True
def cw(board):
    global gr
    if ch(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gr=False
    elif cv(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gr=False
    elif cd(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gr=False
def ct(board):
    global gr
    if "-" not in board:
        printBoard(board)
        print("It is a tie")
        gr=False
def sp():
    global cp
    if cp=='X':
        cp='O'
    else:
        cp='X'
def computer(board):
    while cp=='O':
        pos=random.randint(0,8)
        if board[pos]=="-":
            board[pos]
            sp()
while gr:
    printBoard(board)
    player(board)
    cw(board)
    ct(board)
    if gr==True:
        sp()
        computer(board)
        cw(board)
        ct(board)
