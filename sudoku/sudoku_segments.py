import num_square as sq
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
        for count, tile in enumerate(self.board_list):
            row_num = 'r' + str(num_index)
            self.row_dict[row_num].append(tile)
            if (count+1) % 9 == 0:
                num_index += 1

    def set_cols(self):
        num_index = 1
        for count, tile in enumerate(self.board_list):
            col_num = 'c' + str(num_index)
            self.col_dict[col_num].append(tile)
            num_index += 1
            if (count+1) % 9 == 0:
                num_index = 1

    
    def check_element(self, element, square_num):
        #import pdb; pdb.set_trace()
        tile_row = self.get_segment_nums(self.row_dict[element.tile_elements['tileRow']])
        tile_col = self.get_segment_nums(self.col_dict[element.tile_elements['tileColumn']])
        tile_square = self.get_segment_nums(self.square_dict[element.tile_elements['tileSquare']])
        print (square_num, tile_col, tile_row, tile_square)
        if square_num in tile_row:
            return True
        if square_num in tile_col:
            return True
        if square_num in tile_square:
            return True
        return False



    def set_adjecent_elements(self, element):
        #import pdb; pdb.set_trace()
        element_num1 = element.label[0]
        element_num2 = element.label[1]
        element.tile_elements['tileRow'] = 'r' + element_num1
        element.tile_elements['tileColumn'] = 'c' + element_num2
        element_square = self.find_element_square(element.label)
        element.tile_elements['tileSquare'] = element_square

    def find_element_square(self, element_label):
        element_num1 = int(element_label[0])
        element_num2 = int(element_label[1])
        if element_num2 <= 3:
            if element_num1 <= 3:
                return 's1'
            elif element_num1 > 3 and element_num1 <= 6:
                return 's4'
            elif element_num1 > 6:
                return 's7'
        elif element_num2 > 3 and element_num2 <= 6:
            if element_num1 <= 3:
                return 's2'
            elif element_num1 > 3 and element_num1 <= 6:
                return 's5'
            elif element_num1 > 6:
                return 's8'
        elif element_num2 > 6:
            if element_num1 <= 3:
                return 's3'
            elif element_num1 > 3 and element_num1 <= 6:
                return 's6'
            elif element_num1 > 6:
                return 's9'



    def set_squares(self):
        num_index = 1
        square_base = 1
        for count, tile in enumerate(self.board_list):
            square_num = 's' + str(num_index)
            self.square_dict[square_num].append(tile)
            if (count+1) % 3 == 0:
                num_index += 1
            if (count+1) % 9 == 0:
                num_index = square_base
            if (count+1) % 27 == 0:
                square_base += 3
                num_index = square_base


    def set_square_labels(self):
        row_num = 1
        col_num = 1
        for square in self.board_list:
            square.label = str(row_num) + str(col_num)
            self.set_adjecent_elements(square)
            col_num += 1
            if col_num % 10 == 0:
                col_num = 1
                row_num += 1


    def set_board(self):
        self.set_square_labels()
        self.segment_keys = [x for x in self.row_dict.keys()]
        self.segment_keys.extend([x for x in self.col_dict.keys()])
        self.segment_keys.extend([x for x in self.square_dict.keys()])
        self.set_rows()
        self.set_cols()
        self.set_squares()
        while self.segment_keys:
            segment_index = random.randint(0, len(self.segment_keys)-1)
            segment = self.segment_keys.pop(segment_index)
            self.set_segment(str(segment))
        self.print_board()

    def get_segment_piece(self, game_segment, number_to_set):
        for key, value in game_segment:
            if key[1] == number_to_set:
                return value

    def get_segment_nums(self, segment):
        num_list = []
        for tile in segment:
            num_list.append(tile.square_num)
        return num_list

    def set_segment(self, segment):
        if segment[0] == 'r':
            game_segment = self.row_dict[segment]
        elif segment[0] == 'c':
            game_segment = self.col_dict[segment]
        else:
            game_segment = self.square_dict[segment]
        segment_nums = self.get_segment_nums(game_segment)
        nums_to_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 
        while '0' in segment_nums:
            choose_index = True
            
            set_num_index = random.randint(0, len(nums_to_set)-1)
            #print(nums_to_set, len(nums_to_set)-1,set_num_index)
            try:
                set_num = nums_to_set[set_num_index]
            except:
                print('set_num1')
                import pdb; pdb.set_trace()
            if set_num in segment_nums and set_num in nums_to_set:
                try:
                    nums_to_set.remove(set_num)
                except:
                    print('nums to remove')
                    import pdb; pdb.set_trace()
            
            
            try:
                piece_to_set = random.randint(0, 8)
                game_piece = game_segment[int(piece_to_set)]
                while game_piece.square_num != '0':
                    #import pdb; pdb.set_trace()
                    piece_to_set = random.randint(0, 8)
                    game_piece = game_segment[int(piece_to_set)]
            except Exception:
                #import pdb; pdb.set_trace()
                print('error!')
            while choose_index:
                choose_index = self.check_element(game_piece, set_num)
                if not choose_index:
                    if set_num in nums_to_set:
                        nums_to_set.remove(set_num)
                    break
                else:
                    set_num_index = random.randint(0, len(nums_to_set)-1)
                    #print(nums_to_set, len(nums_to_set)-1,set_num_index)
                    try:
                        set_num = nums_to_set[set_num_index]
                        print ('in else', nums_to_set)
                    except:
                        print('set num2')
                        import pdb; pdb.set_trace()
                    
            if game_piece.square_num == '0':
                game_piece.square_num = set_num
            else:
                if game_piece.square_num in nums_to_set:
                    nums_to_set.remove(game_piece.square_num)
            segment_nums = self.get_segment_nums(game_segment)

    def print_board(self):
        print_string = ''
        for count, square in enumerate(self.board_list):
            print_string += ' ' + str(square) + ' '
            if (count+1) % 3 == 0 and (count+1) % 9 != 0:
                print_string += '  '
            if (count+1) % 9 == 0:
                print(print_string)
                print_string = ''
            if (count+1) % 27 == 0:
                print(print_string)
                print('\n')
                print_string = ''
        for tile in self.board_list:
            print(tile.label, ':', tile.tile_elements)
