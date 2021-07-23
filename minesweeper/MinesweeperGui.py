from guizero import App, PushButton, Text, Box, Window, Picture
from GameBoard import GameBoard
import math
import copy

app = App(title='Minesweeper', layout='grid')
app.tk.borderwidth=5
window = Window(app, title='Minesweeper')#, layout='grid')
tileButtonDict = {}
textDict = {}
mineDict = {}
tileDictionary = {}
tileList = []
gameBoard = 'global init'
board = Box(window, height=500, width=500, layout='grid')#=[0,0])
""" 
board.bg = 'red'
clear_top = Box(app, height=300, width=5000, grid=[0,0])
clear_top.bg = 'blue'
clear_left = Box(app, height=400, width=500, grid=[0,1])
clear_left.bg = 'blue'
clear_bottom = Box(app, height=300, width=5000, grid=[0,2])
clear_bottom.bg = 'blue'
"""
board.tk.pack(fill="none", expand=True)
mainMen = Box(app, height=300, width=500, grid=[1,1])
mainMen.tk.pack(fill="none", expand=True)

difficulty = ''




def createGame(difficulty):
    global tileList, tileDictionary, gameBoard

    gameBoard = GameBoard()
    tileList = gameBoard.createBoard(difficulty)
    
    tileDictionary = copy.deepcopy(gameBoard.tileDictionary)
  



def playGame(tile):

    global gameBoard
  
    if not tile.isMarked:

        if tile.isMined:
         
            gameOver(False)
         
        else:

            uncoverList = gameBoard.tileAction(tile.label,'uncover')
            uncoverTiles(uncoverList)

            if len(gameBoard.tileDictionary) == gameBoard.numMines:

                gameOver(True)
    

def uncoverTiles(uncoverList):

    global tileButtonDict
    
    tempList = []
    for tile in uncoverList:
        tempList.append(tile.label)
   
    for tile in uncoverList:

        if tile.label in tileButtonDict.keys():
        
            uncoverTileButton = tileButtonDict.get(tile.label)
          
            #surroundingMines = Text(board, text=str(tile), grid=uncoverTileButton.grid)
            #surroundingMines.height = 2
            #surroundingMines.width = 2
            #textDict[tile.label] = surroundingMines
        
            uncoverTileButton.destroy()
            del tileButtonDict[tile.label]
           

def gameOver(win):

    global board, tileButtonDict, tileDictionary

    tempDict = {}

    for tileButton in tileButtonDict:
    
        gameTileButton = tileButtonDict[tileButton]
        gameTile = tileDictionary[tileButton]
        

        if win and gameTile.isMined:
            
            gameTileButton.disable()
            gameTileButton.image = 'danger.jpg'
            
        elif not win and gameTile.isMined:
               
            
            #picture = Picture(board, image='bomb2.jpg', grid=gameTileButton.grid)
           
            #picture.height = 25
            #picture.width = 15
            #mineDict[tileButton] = picture
            gameTileButton.destroy()
            tempDict[tileButton] = tileButtonDict[tileButton]
           
            
        else:
            
            text = Text(board, text=gameTile.surroundingMineCount, grid=gameTileButton.grid)
            text.height = 2
            text.width = 3
            textDict[tileButton] = text
            gameTileButton.destroy()
            tempDict[tileButton] = tileButtonDict[tileButton]

    for tileButton in tempDict:

        del tileButtonDict[tileButton]

def markTile(button):

    global tileDictionary, tileButtonDict, gameBoard
    tileLabel = ''
    
    for key, tileButton in tileButtonDict.items():
        
        if tileButton == button.widget:

            tileLabel = key
    
    markTile = tileDictionary[tileLabel]
    
    marked = gameBoard.tileAction(markTile.label,'mark')
    
    if marked:

        (button.widget).image = 'danger.jpg'

    else:

        (button.widget).image = 'blank.jpg'

def clearBoard():

    global tileButtonDict, textDict, mineDict
    print('text dict', textDict)
    for text in textDict:

        print('text key', text)
        print('text value',textDict[text])
        textDict[text].destroy()
        print ('after destroy')
    for pic in mineDict:

        mineDict[pic].destroy()
    print (tileButtonDict)
    for button in tileButtonDict:
        print(button)
        tileButtonDict[button].destroy()

    tileButtonDict = {}
    textDict = {}
    mineDict = {}

def reset():

    clearBoard()
    showBoard()

def goToMain():

    global difficulty

    clearBoard()
    difficulty = ''
    window.hide()
    app.show()

def showBoard():
   
    global board, tileButtonDict, tileList, gameBoard, difficulty
    createGame(difficulty)
    

    rowLabelCount = 0
    columnLabelCount = 0

    if len(tileList) > 256:
        
        rowLength = int(len(tileList)/16)

    else:

        rowLength = math.sqrt(len(tileList)) 
        
    rowCount = 0
    columnCount = 0
  
    for tile in tileList:

        if not tile.isMined:

            surroundingMines = Text(board, text=str(tile.surroundingMineCount), grid=[columnCount,rowCount])
            surroundingMines.height = 2
            surroundingMines.width = 3
            textDict[tile.label] = surroundingMines

        else:

            picture = Picture(board, image='bomb2.jpg', grid=[columnCount,rowCount])   
            picture.height = 25
            picture.width = 15
            mineDict[tile.label] = picture
        
        tileButton = PushButton(board, command=playGame, image = "blank.jpg" , args=[tile], grid=[columnCount,rowCount], text='')#str(tile)#.isMined))#str(tile))
        tileButton.bg = 'gray60'
        #print ('button grid', tileButton.grid)
        tileButton.when_right_button_pressed = markTile
        tileButton.width = 32
        tileButton.height = 37
        tileButtonDict[tile.label] = tileButton
        columnCount += 1
            
        if columnCount == rowLength:

            rowCount += 1
            columnCount = 0


def quitGame():

    window.destroy()
    app.destroy()

def startGame(diffLevel):
    
    global difficulty

    difficulty = diffLevel
    app.hide()
    window.show()
    showBoard()

resetButton = PushButton(window, width=12, command=reset, text=' RESET ', grid=[0,0])
resetButton.bg = 'gray80'
mainMenuButton = PushButton(window, width=12, command=goToMain, text=' MAIN MENU ', grid=[8,5])
mainMenuButton.bg = 'gray80'
quitWinButton = PushButton(window, width=12, command=quitGame, text=' QUIT ',grid=[4,5])
quitWinButton.bg = 'gray80'
 
#button_box = Box(app, height=500, width=500, grid=[0,1])
begButton = PushButton(mainMen, command=startGame,args=['beginner'], width=12, text=' BEGINNER ', grid=[0,0])
begButton.bg = 'gray80'
intButton = PushButton(mainMen, command=startGame,args=['intermediate'], width=12, text=' INTERMEDIATE ', grid=[0,1])
intButton.bg = 'gray80'
expButton = PushButton(mainMen, command=startGame,args=['expert'], width=12, text=' EXPERT ', grid=[0,2])
expButton.bg = 'gray80'
quitAppButton = PushButton(mainMen, command=quitGame, width=12, text=' QUIT ', grid=[0,4])
quitAppButton.bg = 'gray80'
""" 
picBox = Box(app,  height=500, width=500, grid=[2,0])
picture = Picture(mainMen, image='lose2.jpg', grid=[30,0])           
picture.height = 100
picture.width = 100
"""
app.tk.attributes("-fullscreen",True)
window.tk.attributes("-fullscreen",True)
window.hide()
app.display()