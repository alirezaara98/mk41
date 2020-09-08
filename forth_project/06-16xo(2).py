# XO second version
from random import randint
board = [['-','-','-'],['-','-','-'],['-','-','-']]
counter = 0

number = input("enter number between 1 to 9: ")


def move():
    global number
    if int(number) in [1,2,3]:
        if board[0][int(number)-1] == '-':
            board[0][int(number)-1] = board[0][int(number) - 1].replace('-','o')
        else:
            number = input("enter number between 1 to 9: ")
            move()
    elif int(number) in [4,5,6]:
        if board[1][int(number)-4] == '-':
            board[1][int(number) - 4] = board[1][int(number)-4].replace('-','o')
        else:
            number = input("enter number between 1 to 9: ")
            move()
    else:
        if board[2][int(number)-7] == '-':
            board[2][int(number) - 7] = board[2][int(number)-7].replace('-','o')
        else:
            number = input("enter number between 1 to 9: ")
            move()
    return number

def auto_os_move():
    auto = randint(1,9)
    if auto in [1,2,3]:
        if board[0][auto-1] == '-':
            board[0][auto - 1] = board[0][auto-1].replace('-','x')
        else:
            auto_os_move()
    elif auto in [4,5,6]:
        if board[1][auto-4] == '-':
            board[1][auto - 4] = board[1][auto-4].replace('-','x')
        else:
            auto_os_move()
    else:
        if board[2][auto -7] == '-':
            board[2][auto - 7] = board[2][auto -7].replace('-','x')
        else:
            auto_os_move()
    return

def os_move(number):
    user_place = int(number)
    # first situation
    if user_place == 1:
        # place in 5,2,4
        if board[1][1] == '-':
            board[1][1] = board[1][1].replace('-', 'x')
        elif board[0][1] == '-':
            board[0][1] = board[0][1].replace('-', 'x')
        elif board[1][0] == '-':
            board[1][0] = board[1][0].replace('-', 'x')
        #other placement
        else:
            auto_os_move()
    # second situation
    elif user_place == 2:
        # place in 1,3,5,4,6
        if board[0][0] == '-':
            board[0][0] = board[0][0].replace('-', 'x')
        elif board[0][2] == '-':
            board[0][2] = board[0][2].replace('-', 'x')
        elif board[1][1] == '-':
            board[1][1] = board[1][1].replace('-', 'x')
        elif board[1][0] == '-':
            board[1][0] = board[1][0].replace('-', 'x')
        elif board[1][2] == '-':
            board[1][2] = board[1][2].replace('-', 'x')
        # other placement
        else:
            auto_os_move()
    # third situation
    elif user_place == 3:
        # place in 5,2,6
        if board[1][1] == '-':
            board[1][1] = board[1][1].replace('-','x')
        elif board[0][1] == '-':
            board[0][1] = board[0][1].replace('-','x')
        elif board[1][2] == '-':
            board[1][2] = board[1][2].replace('-','x')
        # other placement
        else:
            auto_os_move()
    # forth situation
    elif user_place == 4:
        # place in 1,5,7,2,8
        if board[0][0] == '-':
            board[0][0] = board[0][0].replace('-','x')
        elif board[1][1] == '-':
            board[1][1] = board[1][1].replace('-','x')
        elif board[2][0] == '-':
            board[2][0] = board[2][0].replace('-','x')
        elif board[0][1] == '-':
            board[0][1] = board[0][1].replace('-','x')
        elif board[2][1] == '-':
            board[2][1] = board[2][1].replace('-','x')
        # other placement
        else:
            auto_os_move()
    # fifth situation
    elif user_place == 5:
        for movement in [4,6,2,8,1,3,7,9]:
            if movement in [1,2,3]:
                if board[0][movement-1] == '-':
                    board[0][movement - 1] = board[0][movement-1].replace('-','x')
                    return
            elif movement in [4,6]:
                if board[1][movement-4] == '-':
                    board[1][movement - 4] = board[1][movement-4].replace('-','x')
                    return
            else:
                if board[2][movement-7] == '-':
                    board[2][movement - 7] = board[2][movement-7].replace('-','x')
                    return
    # sixth situation
    elif user_place == 6:
        # place in 3,5,9,8,2
        if board[0][2] == '-':
            board[0][2] = board[0][2].replace('-','x')
        elif board[1][1] == '-':
            board[1][1] = board[1][1].replace('-','x')
        elif board[2][2] == '-':
            board[2][2] = board[2][2].replace('-','x')
        elif board[2][1] == '-':
            board[2][1] = board[2][1].replace('-','x')
        elif board[0][1] == '-':
            board[0][1] = board[0][1].replace('-','x')
        # other placement
        else:
            auto_os_move()
    # seventh situation
    elif user_place == 7:
        # place in 5,4,8
        if board[1][1] == '-':
            board[1][1] = board[1][1].replace('-','x')
        elif board[1][0] == '-':
            board[1][0] = board[1][0].replace('-','x')
        elif board[2][1] == '-':
            board[2][1] = board[2][1].replace('-','x')
        # other placement
        else:
            auto_os_move()
    # eighth situation
    elif user_place == 8:
        # place in 7,5,9,4,6
        if board[2][0] == '-':
            board[2][0] = board[2][0].replace('-','x')
        elif board[1][1] == '-':
            board[1][1] = board[1][1].replace('-','x')
        elif board[2][2] == '-':
            board[2][2] = board[2][2].replace('-','x')
        elif board[1][0] == '-':
            board[1][0] = board[1][0].replace('-','x')
        elif board[1][2] == '-':
            board[1][2] = board[1][2].replace('-','x')
        # other placement
        else:
            auto_os_move()
    # ninth situation
    else:
        # place in 5,6,8
        if board[1][1] == '-':
            board[1][1] = board[1][1].replace('-','x')
        elif board[1][2] == '-':
            board[1][2] = board[1][2].replace('-','x')
        elif board[2][1] == '-':
            board[2][1] = board[2][1].replace('-','x')
        # other placement
        else:
            auto_os_move()
    return

while counter <10 :
    if counter == 8:
        move()
    else:
        move()
        os_move(number)
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







