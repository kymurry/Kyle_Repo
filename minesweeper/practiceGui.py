from guizero import App, PushButton, Text, Box, Window, Picture


app = App(height=1000, width=1000)
board1 = Box(app, height=50, width=50)
board1.tk.grid = [0,0]
board1.bg = 'red'
board2 = Box(app, height=50, width=50)
board2.bg = 'blue'
board2.tk.grid = [1,2]
board3 = Box(app, height=50, width=50)
board3.tk.grid = [1,1]
board3.bg = 'green'
board3 = Box(app, height=50, width=50)
board3.bg = 'yellow'
board4 = Box(app, height=50, width=50)
board4.tk.grid = [1,3]
picture = Picture(board4, image='lose2.jpg')           
picture.height = 50
picture.width = 50

#board3.bg = 'green'

#picture = Picture(app, image='lose2.jpg', grid=[0,0])

#picture = Picture(app, image='lose2.jpg', grid=[0,2, 10, 3])




app.display()