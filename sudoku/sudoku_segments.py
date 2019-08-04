import sudoku.num_square as sq
import random

class gameBoard(object):

    def __init__(self):
        self.board_list = [sq.SoTile() for x in range(9*9)]
        self.row_dict = {'r1': [], 'r2': [], 'r3': [], 'r4': [], 'r5': [], 'r6': [], 'r7': [], 'r8': [], 'r9': []}
        self.col_dict = {'c1': [], 'c2': [], 'c3': [], 'c4': [], 'c5': [], 'c6': [], 'c7': [], 'c8': [], 'c9': []}
        self.square_dict = {'s1': [], 's2': [], 's3': [], 's4': [], 's5': [], 's6': [], 's7': [], 's8': [], 's9': []}
        self.segment_keys = []

    def set_rows(self):
        num_index = 1
        import pdb;pdb.set_trace()
        for count, tile in enumerate(self.board_list):
            row_num = 'r' + str(num_index)
            self.row_dict[row_num].append(tile)
            if (count+1) % 9 == 0:
                num_index += 1

    def set_cols(self):
        num_index = 1
        for count, tile in enumerate(self.board_list):
            row_num = 's' + str(num_index)
            self.row_dict[row_num].append(tile)
            num_index += 1
            if (count+1) % 9 == 0:
                num_index = 1

    def set_squares(self):
        num_index = 1
        for count, tile in enumerate(self.board_list):
            row_num = 's' + str(num_index)
            self.row_dict[row_num].append(tile)
            if (count+1) % 3 == 0:
                num_index += 1
            if (count+1) % 9 == 0:
                num_index = 1

    def set_board(self):
        #import pdb; pdb.set_trace()
        self.segment_keys = [x for x in self.row_dict.keys()]
        self.segment_keys.extend([x for x in self.col_dict.keys()])
        self.segment_keys.extend([x for x in self.square_dict.keys()])
        self.set_rows
        self.set_cols
        self.set_squares
        segment_index = random.randint(0, len(self.segment_keys)-1)
        segment = self.segment_keys.pop(segment_index)
        self.set_segment(str(segment))

    def get_segment_piece(self, game_segment, number_to_set):
        for key, value in game_segment:
            if key[1] == number_to_set:
                return value

    def set_segment(self, segment):
        #import pdb;pdb.set_trace()
        if segment[0] == 'r':
            game_segment = self.row_dict[segment]
        elif segment[0] == 'c':
            game_segment = self.col_dict[segment]
        else:
            game_segment = self.square_dict[segment]
        nums_to_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 
        while nums_to_set:
            set_num_index = random.randint(0, len(nums_to_set)-1)
            set_num = nums_to_set.pop(set_num_index)
            segment_piece_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            segment_piece_index = random.randint(0, len(segment_piece_nums)-1)
            import pdb; pdb.set_trace()
            piece_to_set = segment_piece_nums.pop(segment_piece_index)
            game_piece = game_segment[piece_to_set]
            if game_piece.square_num == '0':
                game_piece.square_num = set_num
            else:
                if game_piece.square_num in nums_to_set:
                    nums_to_set.remove(game_piece.square_num)

    def print_board(self):
        for count, square in enumerate(self.board_list):
            print(' ', square, ' ')
            if count % 3 == 0 and count % 9 != 0:
                print('  ')
            if count % 9 == 0 and count % 3 != 0:
                print('\n')
            if count % 9 == 0 and count % 3 == 0:
                print('\n')
                print('\n')
