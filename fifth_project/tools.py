def checker(start, color, step, move_type, board):
    move_list = []
    if color == 'B':
        if move_type == 'forward':
            mtype = 'backward'
        else:
            mtype = 'forward'
    else:
        mtype = move_type
    if mtype == 'forward':
        index = start - step
        while index >= 0:
            if '*' not in board[index]:
                move_list.append(index)
                break
            move_list.append(index)
            index -= step
    elif mtype == 'backward':
        index = start + step
        while index <= 63:
            if '*' not in board[index]:
                move_list.append(index)
                break
            move_list.append(index)
            index += step
    return move_list


def move_check(board, final_dict, color,  *places_list):
    for place_list in places_list:
        if place_list:
            for place_index in place_list:
                if '*' in board[place_index]:
                    final_dict['empty_place'].append(board[place_index][:2])
                elif color not in board[place_index]:
                    final_dict['attack'].append(board[place_index][:2])
                else:
                    pass
        else:
            continue
    return final_dict


def rook_lr_move(start, move_type, board):
    move_list = []
    if move_type == 'left':
        index = start - 1
        while index >= start - 7 and 0 <= index <= 63:
            if '*' not in board[index]:
                move_list.append(index)
                break
            move_list.append(index)
            index -= 1
    elif move_type == 'right':
        index = start + 1
        while index <= start + 7 and 0 <= index <= 63:
            if '*' not in board[index]:
                move_list.append(index)
                break
            move_list.append(index)
            index += 1
    else:
        pass
    return move_list
