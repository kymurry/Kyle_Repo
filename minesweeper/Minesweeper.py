from GameBoard import GameBoard
import math

gameBoard = []

difficultyChoices = ['beginner','intermediate','expert']
playChoices = ['mark', 'unmark', 'uncover', 'exit']

def startGame(difficulty):

    gameBoard = GameBoard()
    tileList = gameBoard.createBoard(difficulty)
    playGame(gameBoard)

def playGame(gameBoard):

    tileDict = gameBoard.tileDictionary
    printBoard = True
    
    playList = ['exit']

    for tile in gameBoard.tileDictionary.keys():

        playList.append(tile)



    while 1:

        if printBoard:

            gameBoard.printBoard()

        while 1:

            actionTile = str(input('Please pick a tile \n').upper())

            if actionTile not in playList:

                print ('\n')
                print ('You have selected a tile that does not exist!')
                print ('\n')

            elif actionTile == 'exit':

                return False

            else:

                break

        while 1:

            action = str(input('Would you like to mark, unmark, or uncover the tile?\n').lower())

            print('\n')

            if action not in playChoices:

                print ('\n')
                print ('You have chosen an action that is not supported!')
                print ('\n')

                
            elif actionTile == 'exit':

                return False

            else:

                break

        if actionTile in gameBoard.tileDictionary.keys() and action in playChoices:
            
            if (gameBoard.tileDictionary[actionTile]).isMined == True and action == 'uncover':

                gameBoard.gameOver()
                gameBoard.printBoard()

                print ('\n')
                print ('Game Over!')
                print ('\n')

                break

            printBoard = gameBoard.tileAction(actionTile,action)

            winCheck = gameBoard.winCheck()

            if winCheck:

                gameBoard.printBoard()

                print ('\n')
                print ('************************')
                print ('************************')
                print ('************************')
                print ('******* You Win ! ******')
                print ('************************')
                print ('************************')
                print ('************************')
                print ('\n')

                break

    return True

gameFlag = True

while 1:

    if gameFlag == False:

        break

    gameInput = input('Would you like to play a game?\n')
    gameInput = str(gameInput).lower()

    if gameInput == 'yes':

        while 1:
        
            gameParamInput = input('Enter exit at any time if you wish to quit the game, otherwise enter one of the following difficulty levels:  beginner, intermediate, or expert.\n')
            gameParamInput = str(gameParamInput).lower()

            if gameParamInput in difficultyChoices:

                gameFlag = startGame(gameParamInput)

                break

            elif gameParamInput == 'exit':

                gameFlag = False
               
                break

            else:

                print ('Please enter a difficulty level or exit the game.')

    elif gameInput == 'no':

        print ('Goodbye')

        break

    else:

        print('Please answer with yes or no.')