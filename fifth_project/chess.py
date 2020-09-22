from projects.fifth_project.tools import checker, move_check, rook_lr_move


class Board:
    primary_board = ['1aRB', '1bHB', '1cBSB', '1dQB', '1eKB', '1fBSB', '1gHB', '1hRB',
                     '2aPB', '2bPB', '2cPB', '2dPB', '2ePB', '2fPB', '2gPB', '2hPB',
                     '3a**', '3b**', '3c**', '3d**', '3e**', '3f**', '3g**', '3h**',
                     '4a**', '4b**', '4c**', '4d**', '4e**', '4f**', '4g**', '4h**',
                     '5a**', '5b**', '5c**', '5d**', '5e**', '5f**', '5g**', '5h**',
                     '6a**', '6b**', '6c**', '6d**', '6e**', '6f**', '6g**', '6h**',
                     '7aPW', '7bPW', '7cPW', '7dPW', '7ePW', '7fPW', '7gPW', '7hPW',
                     '8aRW', '8bHW', '8cBSW', '8dQW', '8eKW', '8fBSW', '8gHW', '8hRW']
    resetting_board = primary_board.copy()

    def __init__(self):
        self.board = Board.primary_board

    @staticmethod
    def guide():
        print('\t       ***********base guide***********')
        print('place guide:\n <number of place><name of place><piece name><color> --> like "1aBSB"')
        print('use these names instead of fullname\n !!!use string format\n !!! * means empty')
        print('colors: \n white --> W \n black --> B')
        print(
            'piece name:\n rook --> R\n horse --> H\n bishop --> BS\n queen --> Q\n king --> K\n pawn --> P')
        return

    def get_board(self):
        print('board:')
        print("\t\ta\t\tb\t\tc\t\td\t\te\t\tf\t\tg\t\th")
        print('1\t' + str(self.board[0:8]).strip('[]'))
        print('2\t' + str(self.board[8:16]).strip('[]'))
        print('3\t' + str(self.board[16:24]).strip('[]'))
        print('4\t' + str(self.board[24:32]).strip('[]'))
        print('5\t' + str(self.board[32:40]).strip('[]'))
        print('6\t' + str(self.board[40:48]).strip('[]'))
        print('7\t' + str(self.board[48:56]).strip('[]'))
        print('8\t' + str(self.board[56:64]).strip('[]'))
        return

    def reset_board(self):
        self.board = Board.resetting_board


class Square(Board):

    def __init__(self, name, color, location):
        super().__init__()
        self.name = name
        self.location = location
        self.color = color

    def piece_color(self):
        print(self.color)
        return

    def piece_name(self):
        print(self.name)
        return

    def square_color(self):
        for block in self.board:
            if self.location in block:
                if self.board.index(block) % 2 == 0:
                    print('black')
                    return
                else:
                    print('white')
                    return


class Piece(Square):
    placelist = []
    place_name_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    start_index = None

    def __init__(self, name, color, location):
        super().__init__(name, color, location)
        for place in self.board:
            if f"{self.name}{self.color}" in place:
                Piece.placelist.append(place)
        self.place = Piece.placelist

    def set_start_index(self):
        for block in self.board:
            if self.location in block:
                Piece.start_index = self.board.index(block)
                break

    def move(self, target):
        for block in self.board:
            if self.location in block:
                self.board[self.board.index(block)] = block.replace(block[2:], '**')
            if target in block:
                self.board[self.board.index(block)] = block.replace(block[2:], f'{self.name}{self.color}')


class King(Piece):
    def __init__(self, name, color, location):
        super().__init__(name, color, location)

    def movement_list(self):
        possible_place = {'attack': [], 'empty_place': []}
        for index in [Piece.start_index - 8, Piece.start_index - 7, Piece.start_index - 9, Piece.start_index + 8,
                      Piece.start_index + 9, Piece.start_index + 7, Piece.start_index + 1, Piece.start_index - 1]:
            if 0 <= index < 64:
                if '*' in self.board[index]:
                    possible_place['empty_place'].append(self.board[index][:2])
                elif self.color not in self.board[index]:
                    possible_place['attack'].append(self.board[index][:2])
                else:
                    pass
        print(possible_place)
        return


class Queen(Piece):

    def __init__(self, name, color, location):
        super().__init__(name, color, location)

    def movement_list(self):
        possible_place = {'attack': [], 'empty_place': []}
        name_index = Piece.place_name_list.index(self.location[1])
        sevenforward_templist = checker(Piece.start_index, self.color, 7, 'forward', self.board)
        sevenbackward_templist = checker(Piece.start_index, self.color, 7, 'backward', self.board)
        eightforward_templist = checker(Piece.start_index, self.color, 8, 'forward', self.board)
        eightbackward_templist = checker(Piece.start_index, self.color, 8, 'backward', self.board)
        nineforward_templist = checker(Piece.start_index, self.color, 9, 'forward', self.board)
        ninebackward_templist = checker(Piece.start_index, self.color, 9, 'backward', self.board)
        if self.color == 'B':
            sevenforward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[:name_index],
                       sevenforward_templist))
            sevenbackward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[name_index + 1:],
                       sevenbackward_templist))
            eightforward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[name_index], eightforward_templist))
            eightbackward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[name_index], eightbackward_templist))
            nineforward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[name_index + 1:], nineforward_templist))
            ninebackward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[:name_index], ninebackward_templist))
        else:
            sevenforward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[name_index + 1:], sevenforward_templist))
            sevenbackward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[:name_index], sevenbackward_templist))
            eightforward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[name_index], eightforward_templist))
            eightbackward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[name_index], eightbackward_templist))
            nineforward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[:name_index], nineforward_templist))
            ninebackward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[name_index + 1:], ninebackward_templist))
        possible_place.update(
            move_check(self.board, possible_place, self.color, sevenforward_list, sevenbackward_list,
                       eightforward_list,
                       eightbackward_list, nineforward_list, ninebackward_list))
        print(possible_place)
        return


class Bishop(Piece):

    def __init__(self, name, color, loction):
        super().__init__(name, color, loction)

    def movement_list(self):
        possible_place = {'attack': [], 'empty_place': []}
        name_index = Piece.place_name_list.index(self.location[1])
        sevenforward_templist = checker(Piece.start_index, self.color, 7, 'forward', self.board)
        sevenbackward_templist = checker(Piece.start_index, self.color, 7, 'backward', self.board)
        nineforward_templist = checker(Piece.start_index, self.board, 9, 'forward', self.board)
        ninebackward_templist = checker(Piece.start_index, self.color, 9, 'backward', self.board)
        if self.color == 'B':
            sevenforward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[:name_index],
                       sevenforward_templist))
            sevenbackward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[name_index + 1:],
                       sevenbackward_templist))
            nineforward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[name_index + 1:], nineforward_templist))
            ninebackward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[:name_index], ninebackward_templist))
        else:
            sevenforward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[name_index + 1:], sevenforward_templist))
            sevenbackward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[:name_index], sevenbackward_templist))
            nineforward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[:name_index], nineforward_templist))
            ninebackward_list = list(
                filter(lambda index: self.board[index][1] in Piece.place_name_list[name_index + 1:], ninebackward_templist))
        possible_place.update(
            move_check(self.board, possible_place, self.color, sevenforward_list, sevenbackward_list,
                       nineforward_list,
                       ninebackward_list))
        print(possible_place)
        return


class Horse(Piece):
    def __init__(self, name, color, location):
        super().__init__(name, color, location)

    def movement_list(self):
        possible_place = {'attack': [], 'empty_place': []}
        rl_temp = [Piece.start_index - 6, Piece.start_index + 6, Piece.start_index - 10, Piece.start_index + 10]
        rl_list = list(filter(lambda indx: 0 <= indx < 64 and abs(int(self.location[0]) - int(self.board[indx][0])) == 1, rl_temp))
        for index in [Piece.start_index - 15, Piece.start_index - 17, Piece.start_index + 15, Piece.start_index + 17]+rl_list:
            if 0 <= index < 64:
                if '*' in self.board[index]:
                    possible_place['empty_place'].append(self.board[index][:2])
                elif self.color not in self.board[index]:
                    possible_place['attack'].append(self.board[index][:2])
                else:
                    pass
        print(possible_place)
        return


class Rook(Piece):

    def __init__(self, name, color, location):
        super().__init__(name, color, location)

    def movement_list(self):
        possible_place = {'attack': [], 'empty_place': []}
        forward_templist = checker(Piece.start_index, self.color, 8, 'forward', self.board)
        backward_templist = checker(Piece.start_index, self.color, 8, 'backward', self.board)
        left_templist = rook_lr_move(Piece.start_index, 'left', self.board)
        right_templist = rook_lr_move(Piece.start_index, 'right', self.board)
        forward_list = list(filter(lambda indx: self.location[1] in self.board[indx], forward_templist))
        backward_list = list(filter(lambda indx: self.location[1] in self.board[indx], backward_templist))
        left_list = list(filter(lambda indx: self.location[0] in self.board[indx], left_templist))
        right_list = list(filter(lambda indx: self.location[0] in self.board[indx], right_templist))
        possible_place.update(
            move_check(self.board, possible_place, self.color, forward_list, backward_list, left_list,
                       right_list))
        print(possible_place)
        return


class Pawn(Piece):
    def __init__(self, name, color, location):
        super().__init__(name, color, location)

    def movement_list(self):
        possible_place = {'attack': [], 'empty_place': []}
        if self.color == 'B':
            attack_list = list(filter(lambda indx: int(self.board[indx][0]) - int(self.location[0]) == 1,
                                      [Piece.start_index + 9, Piece.start_index + 7]))
            if self.location[0] == '2' and '*' in self.board[Piece.start_index + 8]:
                empty_choice = [Piece.start_index + 8, Piece.start_index + 16]
            else:
                empty_choice = [Piece.start_index + 8]
        else:
            attack_list = list(filter(lambda indx: int(self.board[indx][0]) - int(self.location[0]) == -1,
                                      [Piece.start_index - 9, Piece.start_index - 7]))
            if self.location[0] == '7' and '*' in self.board[Piece.start_index - 8]:
                empty_choice = [Piece.start_index - 8, Piece.start_index - 16]
            else:
                empty_choice = [Piece.start_index - 8]
        for index in attack_list:
            if self.color not in self.board[index] and '*' not in self.board[index]:
                possible_place['attack'].append(self.board[index][:2])
        for place in empty_choice:
            if 0 <= place < 64:
                if '*' in self.board[place]:
                    possible_place['empty_place'].append(self.board[place][:2])
        print(possible_place)
        return


if __name__ == "__main__":
    Board.guide()
    
    board1 = Board()
    
    board1.get_board()
    # test cases
    '''user2 = Pawn('P', 'B', '2a')
    user2.set_start_index()
    user2.movement_list()
    user2.move('3a')
    user2.get_board()
    user2 = Pawn('P', 'B', '3a')
    user2.set_start_index()
    user2.movement_list()
    user = Horse('H', 'W', '8b')
    user.set_start_index()
    user.movement_list()
    user.move('6c')
    user.get_board()
    user = Horse('H', 'W', '6c')
    user.set_start_index()
    user.movement_list()
    user2 = Pawn('p', 'B', '2b')
    user2.set_start_index()
    user2.movement_list()
    user2.move('4b')
    user2.get_board()
    user = Horse('H', 'W', '6c')
    user.set_start_index()
    user.movement_list()
    user.move('4b')
    user.get_board()'''

    '''user = Pawn('P', 'W', '7e')
    user.set_start_index()
    user.movement_list()
    user.move('5e')
    user.get_board()
    user2 = Pawn('P', 'B', '2b')
    user2.set_start_index()
    user2.movement_list()
    user2.move('3b')
    user2.get_board()
    user = Queen('Q', 'W', '8d')
    user.set_start_index()
    user.movement_list()
    user.move('7e')
    user.get_board()
    user2 = Bishop('BS', 'B', '1c')
    user2.set_start_index()
    user2.movement_list()
    user2.move('3a')
    user2.get_board()
    user = Queen('Q', 'W', '7e')
    user.set_start_index()
    user.movement_list()
    user.move('3a')
    user.get_board()'''

    '''user2 = Pawn('P', 'B', '2b')
    user2.set_start_index()
    user2.movement_list()
    user2.move('3b')
    user2.get_board()
    user2 = Bishop('BS', 'B', '1c')
    user2.set_start_index()
    user2.movement_list()'''

    '''user = Pawn('P', 'W', '7g')
    user.set_start_index()
    user.move('6g')
    user.get_board()
    user = Bishop('BS', 'W', '8f')
    user.set_start_index()
    user.movement_list()
    user = Pawn('P', 'W', '7c')
    user.set_start_index()
    user.move('6c')
    user.get_board()
    user = Queen('Q', 'W', '8d')
    user.set_start_index()
    user.movement_list()'''

    '''user = Pawn('P', 'B', '2c')
    user.set_start_index()
    user.move('3c')
    user.get_board()
    user = Queen('Q', 'B', '1d')
    user.set_start_index()
    user.movement_list()
    user.square_color()
    user.reset_board()
    user.get_board()'''

    '''user = Horse('H', 'B', '1g')
    user.set_start_index()
    user.movement_list()
    user.move('3f')
    user.get_board()
    user = Horse('H', 'B', '3f')
    user.set_start_index()
    user.movement_list()'''

    '''user = Pawn('P', 'B', '2h')
    user.set_start_index()
    user.movement_list()
    user.move('4h')
    user.get_board()
    user = Pawn('P', 'B', '4h')
    user.set_start_index()
    user.movement_list()
    user = Rook('R', 'B', '1h')
    user.set_start_index()
    user.movement_list()
    user.move('3h')
    user.get_board()
    user = Rook('R', 'B', '3h')
    user.set_start_index()
    user.movement_list()'''

    '''user = Pawn('P', 'W', '7a')
    user.set_start_index()
    user.movement_list()
    user.move('5a')
    user = Rook('R', 'W', '8a')
    user.set_start_index()
    user.movement_list()
    user.move('6a')
    user.get_board()
    user = Rook('R', 'W', '6a')
    user.set_start_index()
    user.movement_list()'''