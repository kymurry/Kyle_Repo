import num_square as sq
import sudoku_segments as sg
import random

class gameBoard(object):

    def __init__(self):
        self.board_list = [sq.SoTile() for num in range(9*9)]
        self.row_dict = {'r'+ str(num) : sg.SoSegment() for num in range(1,10)}
        self.col_dict = {'c'+ str(num) : sg.SoSegment() for num in range(1,10)}
        self.square_dict = {'s'+ str(num) : sg.SoSegment() for num in range(1,10)}
        self.segment_keys = []
        self.nums_to_set = []
    

    def print(self,element):
        if isinstance(element,list):
            print(*element)
        elif isinstance(element,dict):
            print(*element.values())


    def set_rows(self):
        num_index = 1
        for count, tile in enumerate(self.board_list):
            row_num = 'r' + str(num_index)
            #import pdb; pdb.set_trace()
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

    
    def check_element(self, element, square_num, return_segment = False):
        tile_row = self.row_dict[element.tile_elements['tileRow']].myList
        tile_col = self.col_dict[element.tile_elements['tileColumn']].myList
        tile_square = self.square_dict[element.tile_elements['tileSquare']].myList
        el_check = False
        check_list = []
        print (element.label,square_num, tile_row, tile_col, tile_square)
        print(element.tile_elements['tileRow'], element.tile_elements['tileColumn'], element.tile_elements['tileSquare'])
        if square_num == 0:
            print('Zero')
            return (el_check, None)
        if square_num in tile_row:
            el_check = True
            if return_segment:
                check_list.append(element.tile_elements['tileRow'])
        if square_num in tile_col:
            el_check = True
            if return_segment:
                check_list.append(element.tile_elements['tileColumn'])
        if square_num in tile_square:
            el_check = True
            if return_segment:
                check_list.append(element.tile_elements['tileSquare'])
        print(el_check)
        return (el_check, None) if not check_list else (el_check, check_list)


    def set_adjecent_elements(self, element):
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


    def set_sotile_labels(self):
        row_num = 1
        col_num = 1
        for sotile in self.board_list:
            sotile.label = str(row_num) + str(col_num)
            self.set_adjecent_elements(sotile)
            col_num += 1
            if col_num % 10 == 0:
                col_num = 1
                row_num += 1


    def set_board(self):
        #import pdb; pdb.set_trace()
        self.set_sotile_labels()
        self.segment_keys = list(self.row_dict.keys())
        self.segment_keys.extend(list(self.col_dict.keys()))
        self.segment_keys.extend(list(self.square_dict.keys()))
        self.set_rows()
        self.set_cols()
        self.set_squares()
        while self.segment_keys:
            segment_index = random.randint(0, len(self.segment_keys)-1)
            segment = self.segment_keys[segment_index]
            print('******')
            print('*',segment,'*')
            print('******')
            is_set = self.set_segment(str(segment))
            if is_set == True:
                self.segment_keys.remove(segment)
        self.print_board()
    

    def swap_tiles(self,itteration,sotile,num_to_set,set_segment_label):
        if itteration >= 3:
            import pdb; pdb.set_trace()
            return 0
        tile_square_label = sotile.tile_elements['tileSquare']
        tile_square = self.get_game_segment(tile_square_label)
        segment = self.get_game_segment(set_segment_label)
        tile_list = segment.get_sotiles(-1)
        tile_list.remove(sotile)
        print('set segment',set_segment_label,itteration)
        for tile in tile_list:
            self.print_board()
            temp = tile.square_num
            tile.square_num = 0
            tile1_check = self.check_element(tile,num_to_set)
            print('tile1',tile1_check,temp,num_to_set)
            if tile1_check:
                tile.square_num = temp
                continue
            else:
                tile2_check = self.check_element(sotile,temp)
                print('tile2',tile2_check,sotile.square_num,temp)
                if tile2_check:
                    tile.square_num = temp
                    continue
                else:
                    #import pdb; pdb.set_trace()
                    print('num switch',tile.label,temp,num_to_set)
                    tile.square_num = num_to_set
                    
                    self.nums_to_set.remove(num_to_set)
                    self.print_board()
                    return temp
        if num_to_set in tile_square.myList:
            square_tile_index = tile_square.myList.index(num_to_set)
            sotile.square_num = num_to_set
            square_tile_check = self.check_element
        #return self.swap_tiles(itteration+1,sotile,num_to_set,set_segment_label)
        

    #def swap_tiles(self,itteration,sotile,num_to_set,set_segment_label):


    def get_game_segment(self,segment_label):
        if segment_label[0] == 'r':
            return self.row_dict[segment_label]
        elif segment_label[0] == 'c':
            return self.col_dict[segment_label]
        else:
            return self.square_dict[segment_label]


    def set_segment(self, segment):
        game_segment = self.get_game_segment(segment)
        segment_nums = game_segment.myList
        all_nums = [x for x in range(1,10)]
        self.nums_to_set =  list(set(all_nums) - set(segment_nums))
        zero_list = [x for x in game_segment.get_sotiles(-1) if x.square_num == 0]
        
        while zero_list:
            check_list = []
            print('nums',self.nums_to_set,segment_nums)
            set_num = random.choice(self.nums_to_set)
            game_piece_found = False
            while not game_piece_found:
                #if len(set(check_list)) >= 9:
                 #   break
                #piece_to_set = random.randint(0, 8)
                #import pdb; pdb.set_trace()
                game_piece = random.choice(zero_list)#game_segment.get_sotiles(piece_to_set)
                print('check list',[x.label for x in check_list],[x.label for x in zero_list])
                if len(check_list) == len(zero_list):
                    break
                if game_piece in check_list:
                    continue
                check_list.append(game_piece)
                #if game_piece.square_num != 0:
                #    continue
                segment_check = self.check_element(game_piece, set_num)
                print(game_piece,game_piece.label,segment_check,set_num)
                if segment_check:
                    continue
                else:
                    game_piece_found = True
            if not game_piece_found:
                set_num = self.swap_tiles(0,game_piece,set_num,segment)
                #if set_num == None:
                    #import pdb; pdb.set_trace()
                if set_num == 0:
                    continue
                
            print('game piece',game_piece.label)
            game_piece.square_num = set_num
            print('num remove',self.nums_to_set,set_num)
            if set_num in self.nums_to_set: self.nums_to_set.remove(set_num)
            zero_list.remove(game_piece)
            print(self.nums_to_set)
            self.print_board()
            segment_nums = game_segment.myList
        return True


    def print_board(self):
        print('*************************************************************************************************************************************')
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
        print('*************************************************************************************************************************************')
        #for tile in self.board_list:
        #    print(tile.label, ':', tile.tile_elements)
