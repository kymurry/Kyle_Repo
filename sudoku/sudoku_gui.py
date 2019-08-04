from guizero import App, PushButton, Text, Box, Window, Picture
import math


app = App(title='Minesweeper')#, layout='grid')
game_board = Box(app)
game_board.tk.pack(fill="none", expand=True)#, layout='grid')
button_lock_dict = {}




def incriment_number(button):
    print(button)

    button_lock = button_lock_dict.get(button.widget)
    print ('button Lock',button_lock)
    
    if not button_lock:
        if button.widget.text:

            button_num = int(button.widget.text)

            if button_num < 9:

                button.widget.text = str(button_num + 1)

            else: 
                button.widget.text = ''

        else:

            button.widget.text = '1'

def lock_button(button):

    print('is locked?', button_lock_dict[button.widget])

    if button_lock_dict[button.widget] == True:
        print('im in')
        button.widget.enable()
        button_lock_dict[button.widget] = False

    else:

        button.widget.disable()
        button_lock_dict[button.widget] = True

begButton = PushButton(game_board, width=12, text='')#, grid=[0,0])
begButton.when_left_button_pressed = incriment_number
begButton.when_right_button_pressed = lock_button
begButton.bg = 'gray80'
button_lock_dict[begButton] = False

app.display()