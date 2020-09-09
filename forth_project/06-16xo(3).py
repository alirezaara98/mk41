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
    if user_place in [1, 2, 3]:
        # checking left place
        if user_place - 2 >= 0:
            if board[0][user_place - 2] == '-':
                board[0][user_place - 2] = board[0][user_place - 2].replace('-', 'x')
                return
        # checking right place
        try:
            if board[0][user_place] == '-':
                board[0][user_place] = board[0][user_place].replace('-', 'x')
                return
        except:
            pass
        # checking lower place
        if board[1][user_place - 1] == '-':
            board[1][user_place - 1] = board[1][user_place - 1].replace('-', 'x')
            return
        # checking lower row
        if user_place - 2 >= 0:
            if board[1][user_place - 2] == '-':
                board[1][user_place - 2] = board[1][user_place - 2].replace('-', 'x')
                return
        try:
            if board[1][user_place] == '-':
                board[1][user_place] = board[1][user_place].replace('-', 'x')
                return
        except:
            # other placement
            auto_os_move()
    elif user_place in [4, 5, 6]:
        # checking right place
        try:
            if board[1][user_place - 3] == '-':
                board[1][user_place - 3] = board[1][user_place - 3].replace('-', 'x')
                return
        except:
             pass
         # checking higher place
        if board[0][user_place - 4] == '-':
            board[0][user_place - 4] = board[0][user_place - 4].replace('-', 'x')
            return
        # checking left place
        if user_place - 5 >= 0:
            if board[1][user_place - 5] == '-':
                board[1][user_place - 5] = board[1][user_place - 5].replace('-', 'x')
                return
        # checking lower place
        if board[2][user_place - 4] == '-':
            board[2][user_place - 4] = board[2][user_place - 4].replace('-', 'x')
            return
        # checking lower row
        if user_place - 5 >= 0:
            if board[2][user_place - 5] == '-':
                board[2][user_place - 5] = board[2][user_place - 5].replace('-', 'x')
                return
        try:
            if board[2][user_place - 3] == '-':
                board[2][user_place - 3] = board[2][user_place - 3].replace('-', 'x')
                return
        except:
            pass
        # checking upper row
        if user_place - 5 >= 0:
            if board[0][user_place - 5] == '-':
                board[0][user_place - 5] = board[0][user_place - 5].replace('-', 'x')
                return
        try:
            if board[0][user_place - 3] == '-':
                board[0][user_place - 3] = board[0][user_place - 3].replace('-', 'x')
                return
        except:
            # other placement
            auto_os_move()
    else:
        # checking upper place
        if board[1][user_place - 7] == '-':
            board[1][user_place - 7] = board[1][user_place - 7].replace('-', 'x')
            return
        # checking same row
        if user_place - 8 >= 0:
            if board[2][user_place - 8] and board[2][user_place - 8] == '-':
                board[2][user_place - 8] = board[2][user_place - 8].replace('-', 'x')
                return
        try:
            if board[2][user_place - 6] and board[2][user_place - 6] == '-':
                board[2][user_place - 6] = board[2][user_place - 6].replace('-', 'x')
                return
        except:
            pass
        # checking upper row
        if user_place - 8 >= 0:
            if board[1][user_place - 8] and board[1][user_place - 8] == '-':
                board[1][user_place - 8] = board[1][user_place - 8].replace('-', 'x')
                return
        try:
            if board[1][user_place - 6] and board[1][user_place - 6] == '-':
                board[1][user_place - 6] = board[1][user_place - 6].replace('-', 'x')
                return
        except:
            # other placement
            auto_os_move()

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







