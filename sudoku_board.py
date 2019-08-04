import math
import random
import copy

group_dict = {'r1': [[], list(range(1, 10))], 'r2': [[], list(range(1, 10))], 'r3': [[], list(range(1, 10))], 'r4': [[], list(range(1, 10))], 'r5': [[], list(range(1, 10))], 'r6': [[], list(range(1, 10))], 'r7': [[], list(range(1, 10))], 'r8': [[], list(range(1, 10))], 'r9': [[], list(range(1, 10))], 'c1': [[], list(range(1, 10))], 'c2': [[], list(range(1, 10))], 'c3': [[], list(range(1, 10))], 'c4': [[], list(range(1, 10))], 'c5': [[], list(range(1, 10))], 'c6': [[], list(range(1, 10))], 'c7': [[], list(range(1, 10))], 'c8': [[], list(range(1, 10))], 'c9': [[], list(range(1, 10))], 's1': [[], list(range(1, 10))], 's2': [[], list(range(1, 10))], 's3': [[], list(range(1, 10))], 's4': [[], list(range(1, 10))], 's5': [[], list(range(1, 10))], 's6': [[], list(range(1, 10))], 's7': [[], list(range(1, 10))], 's8': [[], list(range(1, 10))], 's9': [[], list(range(1, 10))]}
base_dict = {}
square_dict = {'s1': [], 's2': [], 's3': [], 's4': [], 's5': [], 's6': [], 's7': [], 's8': [], 's9': []}


def create_squares():

    global base_dict

    label_string = 'abcdefghi'
    col_number = 0
    row_number = 0
    square_number = 0
    square_base = 1
    for row in range(0, 9):
        row_key = 'r' + str(row_number + 1)
        square_number = square_base

        for col in range(0, 9):
            #print ('row num', row_number, label_string[row_number])
            #print ('col num', col_number,label_string[col_number])
            #print ('row key', row_key)
            #print ('row', row)
            #print ('col', col)
            #print ('square base', square_base)
            #print ('square num',square_number)
            col_key = 'c' + str(col_number + 1)
            square_key = 's' + str(square_number)
            #print ('square key', square_key)
            #print ('col key', col_key)
            if col_key not in square_dict[square_key]:
                square_dict[square_key].append(col_key)
            if row_key not in square_dict[square_key]:
                square_dict[square_key].append(row_key)
            label = label_string[row_number] + label_string[col_number]
            base_dict.update({label: [0, [square_key, col_key, row_key]]})
            group_dict[row_key][0].append(label) 
            group_dict[col_key][0].append(label)
            group_dict[square_key][0].append(label)
            #print ('initial',sorted(group_dict))
            if (col + 1) == 9:
                square_number = square_base
            if (col + 1) % 3 == 0:
                square_number += 1
            col_number += 1

        col_number = 0
        row_number += 1
        square_number += 3
        #print('next square num', square_number)
        #print('3 div', (row + 1) % 3)
        if (row + 1) % 3 == 0:
            square_base += 3
            #print('base change', square_base)


def remove_square_num(square_label, num):

    element_list = square_dict[square_label]

    for element in element_list:
        if num in group_dict[element][1]:
            group_dict[element][1].remove(num)


def remove_num(element_label, num, element_called):

    global group_dict, base_dict
    #print('group dict', group_dict)
    remove_list = base_dict[element_label][1]
    #print ('remove', remove_list)
    for element in remove_list:
        #print('el list',group_dict[element][1])
        if num in group_dict[element][1]:
            group_dict[element][1].remove(num)
            #print ('remove',sorted(group_dict))
            #print('element lable1',element,num, element_label, group_dict[element])
        #print('\n')
        """
        if element_label in group_dict[element][0] and num in group_dict[element][1]:

            print('\n')
            print('num', num)
            print('num list', group_dict[element])

            #print('el list', group_dict[element][0])

            print('element lable2',element,num, element_label, element_called)
            #print('num list after', group_dict[element])
            temp_dict.update({element:group_dict[element]})
            group_dict[element][1].remove(num)
            #print('num list', group_dict[element][1])

            #print('element lable after', element_label)
        """
    """
    #print('remove dict', group_dict)
    for key in temp_dict:
        print ('temp dict',key,temp_dict[key])
    """


def get_squares(element):

    element_square_list = []

    for square in square_dict:

        if element in square_dict[square]:

            element_square_list.append(square) 

    return element_square_list


def set_game_squares():

    global group_dict, base_dict
    #print ('dict', group_dict)

    temp_list = list(group_dict.keys())
    print('temp list', temp_list)
    while temp_list:

        element_label_index = random.randint(0, len(temp_list)-1)
        #print ('index', element_label_index, temp_list[element_label_index])
        element_label = temp_list[element_label_index]
        element = group_dict.get(element_label)[0]
        #print ('get',sorted(group_dict))
        #test_list = []

        #for square in element:
            #print (square)
         #   test_list.append((base_dict[square][0],square)) 
        #print('element',element_label, sorted(test_list))
        #print('\n')

        for square in element:

            #print('square', base_dict[square])
            #print (base_dict[square])
            if base_dict[square][0] != 0:
                if base_dict[square][0] in group_dict.get(element_label)[1]:
                    group_dict[element_label][1].remove(base_dict[square][0])
                    #print ('re',element_label[1])
                    #print('index removed', group_dict.get(element_label)[1])
                continue
            else:
                """
                #print (group_dict)
                #print('ex1',group_dict[base_dict[square][1][1]][1] )
                #print('ex2',group_dict[base_dict[square][1][2]][1] )
                #temp_list = []
                compare_list = list(range(1,10))
                #print('\n')
                #print(group_dict[base_dict[square][1][1]][1])
                #print('base',base_dict[square][1])
                #print(group_dict[base_dict[square][1][0]])
                #print(group_dict[base_dict[square][1][1]])
                #print(group_dict[base_dict[square][1][2]])
                #exclude_list = set(compare_list) - set(copy.deepcopy(group_dict[base_dict[square][1][1]][1]))
                #list(exclude_list).extend(set(compare_list) - set(group_dict[base_dict[square][1][2]][1]))
                dirty_exclude_list = copy.deepcopy(group_dict[base_dict[square][1][0]][1])
                dirty_exclude_list.extend(copy.deepcopy(group_dict[base_dict[square][1][1]][1]))
                dirty_exclude_list.extend(copy.deepcopy(group_dict[base_dict[square][1][2]][1]))
                #print('dirty', dirty_exclude_list)
                exclude_list = []
                for num in dirty_exclude_list:
                    if num not in exclude_list:
                        exclude_list.append(num)
                #print ('clean',exclude_list)
                exclude_list = set(compare_list) - set(exclude_list)
                #print ('exclude',exclude_list)
                #exclude_list = [temp_list.append(n) for n in exclude_list if n not in temp_list]
                #print('exclude1',exclude_list)
                square_index = random.randint(0,len(group_dict[element_label][1])-1)
                square_number = group_dict.get(element_label)[1][square_index]
                count = 0
                while True:
                    #print('\n')
                    #print ('count', count)
                    count += 1
                    if count >= 100:
                       break
                    #print ('label',element_label,element_label[0] )
                    if element_label[0] != 's':
                        #print('\n')
                        #print('break')


                        break

                    else:

                        #print('\n')
                        #print ('else')

                        if square_number in exclude_list:


                            #print('number', square_number)

                        else:

                            break
                """
                exclude_list = list(set(list(range(1, 10))) - set(group_dict[base_dict[square][1][0]][1]))
                print('exclude', exclude_list)
                print(element_label, base_dict[square][1][0])
                while True:
                    if len(exclude_list) == 9:
                        import pdb; pdb.set_trace()
                    square_index = random.randint(0, len(group_dict.get(element_label)[1])-1)
                    square_number = group_dict.get(element_label)[1][square_index]
                    if square_number not in exclude_list:
                        break
                    print('exclude', exclude_list)
                    print(len(group_dict.get(element_label)[1])-1, group_dict[element_label][1])
                    print(square_number)
                temp = ''
                col_count = 0
                row_count = 0
                square_count = 0
                #print('random',group_dict.get(element_label)[1][0],group_dict.get(element_label)[1][-1] )
                #print(group_dict.get(element_label)[1])
                #print('rand2', square_index)
                #print('ex list',base_dict[square])
                #print('exclude',exclude_list)

                #print('square number', square_number)

                base_dict[square][0] = square_number
                #print('square 1',element_label,element_label[0])
                #print(group_dict[element_label][1])
                remove_num(square, square_number, element_label)
                #if element_label[0] == 's':
                    #print ('square label', element_label, element_label[0])
                    #remove_square_num(square,square_number)
                #group_dict[element_label][1].remove(square_number)
                import pdb; pdb.set_trace()
                for key in base_dict:

                    #print('row count', row_count)
                    col_count += 1
                    temp = temp + ' ' + key + ' ' + str(base_dict[key][0])
                    #print ('temp', temp)
                    #print('col 3', col_count %3)
                    #print('col count', col_count)
                    if col_count %3 == 0:
                        #print('roger roger')
                        temp = temp + '   '
                    if col_count == 9:
                        #print('col 9')
                        #print('count = 9')
                        print(temp)
                        col_count = 0
                        row_count += 1
                        temp = ''
                        if row_count % 3 == 0:
                            square_count += 1
                            row_count = 0
                            if square_count % 3 == 0:
                                square_count = 0
                                print('--------------------------------------------')
                                continue
                            print('\n')



            #print('square2', base_dict[square])
        #break
        test_list = []
        for square in element:

            test_list.append((base_dict[square],square))
        #print('element',element_label, sorted(test_list))
        #print('\n')
        #print('element after', test_list)       
        #print ('element', element)

        temp_list.remove(temp_list[element_label_index])
#print (sorted(group_dict))


create_squares()
set_game_squares()

#for key in group_dict:
    #print (key,group_dict[key])
#print ('\n')
#print('base dict print')
#print ('\n')

print_num = 1
for num in range(0, 9):
    #print ('s' + str(print_num),len(group_dict['s' + str(print_num)][0]))
    print_num += 1