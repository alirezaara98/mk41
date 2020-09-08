#  XO game
from random import randint
board = [['-','-','-'],['-','-','-'],['-','-','-']]
counter = 0

number = input("enter number between 1 to 9: ")
osnumber = randint(1,9)

def userchoice():
    global number
    if int(number) in [1,2,3]:
        if board[0][int(number)-1] == '-':
            board[0][int(number)-1] = board[0][int(number) - 1].replace('-','o')
        else:
            number = input("enter number between 1 to 9: ")
            userchoice()
    elif int(number) in [4,5,6]:
        if board[1][int(number)-4] == '-':
            board[1][int(number) - 4] = board[1][int(number) - 4].replace('-','o')
        else:
            number = input("enter number between 1 to 9: ")
            userchoice()
    else:
        if board[2][int(number)-7] == '-':
            board[2][int(number)-7] = board[2][int(number) - 7].replace('-','o')
        else:
            number = input("enter number between 1 to 9: ")
            userchoice()
    return

def oschoice():
    global osnumber
    if osnumber in [1,2,3]:
        if board[0][osnumber-1] == '-':
            board[0][osnumber-1] = board[0][osnumber - 1].replace('-','x')
        else:
            osnumber = randint(1,9)
            oschoice()
    elif osnumber in [4,5,6]:
        if board[1][osnumber-4] == '-':
            board[1][osnumber-4] = board[1][osnumber - 4].replace('-','x')
        else:
            osnumber = randint(1, 9)
            oschoice()
    else:
        if board[2][osnumber-7] == '-':
            board[2][osnumber-7] = board[2][osnumber - 7].replace('-','x')
        else:
            osnumber = randint(1, 9)
            oschoice()
    return


while counter <10 :
    if counter == 8:
        userchoice()
    else:
        userchoice()
        oschoice()
    for index in board:
        print(' '.join(index))
    #user wining check
    if board[0] == ['o','o','o'] or board[1] == ['o','o','o'] or board[2] == ['o','o','o']:
        print('user won')
        break
    elif board[0][0] == 'o' and board[1][0] =='o' and board[2][0] == 'o':
        print('user won')
        break
    elif board[0][1] == 'o' and board[1][1] =='o' and board[2][1] == 'o':
        print('user won')
        break
    elif board[0][2] == 'o' and board[1][2] =='o' and board[2][2] == 'o':
        print('user won')
        break
    elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        print('user won')
        break
    elif board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o':
        print('user won')
        break
    # os wining check
    elif board[0] == ['x','x','x'] or board[1] == ['x','x','x'] or board[2] == ['x','x','x']:
        print('os won')
        break
    elif board[0][0] == 'x' and board[1][0] =='x' and board[2][0] == 'x':
        print('os won')
        break
    elif board[0][1] == 'x' and board[1][1] =='x' and board[2][1] == 'x':
        print('os won')
        break
    elif board[0][2] == 'x' and board[1][2] =='x' and board[2][2] == 'x':
        print('os won')
        break
    elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        print('os won')
        break
    elif board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x':
        print('os won')
        break
    # checking number of 'o' for printing tie situation
    else:
        sum_o = 0
        for index in board:
            sum_o += index.count('o')
        if sum_o == 5:
            print('tie result')
    counter += 2
print('end')

