from GameTile import GameTile
import random
import math
class GameBoard(object):

    def __init__(self):

        self.boardSize = 0
        self.numMines = 0

        self.BoardParams = {'beginner':[64, 10],'intermediate':[256, 40],'expert':[576, 99]}
        self.tileList = []
        self.tileDictionary = {}
        self.rowLength = 0

    def createBoard(self, difficulty):

        boardParams = self.BoardParams[str(difficulty)]
        
        self.boardSize = boardParams[0]
        self.numMines = boardParams[1]

        for number in range (0, self.boardSize):

            newGameTile = GameTile()
            self.tileList.append(newGameTile)

        self.setMines()
        self.getAdjacentMines()
        self.setTileLabel()

        for tile in self.tileList:
            
            self.tileDictionary[tile.label] = tile
        
        return (self.tileList)

    def tileAction(self, actionTile, action):
       
        uncoverList = []

        if actionTile in self.tileDictionary.keys():
            
            tile = self.tileDictionary.get(actionTile)

            if action == 'mark' or action == 'unmark':

                tile.isMarked = not tile.isMarked
                printBoard = True
               
                return tile.isMarked
            
            elif action == 'uncover':
            
                if tile.isMarked:
                    
                    printString = 'Sorry you can not uncover a marked tile! Please unmark the tile if you wish to uncover it.'
                
                    printBoard = False
                    return printString

                else:

                    uncoverList = self.getTilesToUncover(tile)
                    self.uncoverTiles(uncoverList)
                    printBoard = True
                    return uncoverList
                
        else:

            printString =  'You have chosen a tile that either does not exist or has already been uncovered.\nPlease pick an existing tile that has not been uncovered.'
            
            printBoard = False
            return printString
        

    def setMines(self):

        minesToSet = self.numMines
        minedList = []

        while minesToSet > 0:

            tileToMine = random.randint(0,len(self.tileList)-1)
          
            if tileToMine not in minedList:
                
                self.tileList[tileToMine].isMined = True
                minedList.append(tileToMine)
                minesToSet -= 1

 
    def winCheck(self):

        winCheckList = []
        winCheckDict = {}

        for tile in self.tileList:

            if (not tile.isMined and not tile.isHidden) or (tile.isMined and tile.isHidden):

                winCheckList.append(True)
                winCheckDict[tile.label] = True

            else:

                winCheckList.append(False)
                winCheckDict[tile.label] = False
       
        if all(winCheckList):

            return True

        else:

             return False
        

    def getAdjacentMines(self):

        rowLength = math.sqrt(len(self.tileList))
        if len(self.tileList) > 256:
        
            self.rowLength = int(len(self.tileList)/16)

        else:

            self.rowLength = math.sqrt(len(self.tileList)) 
        
        tileIndex = 0
        leftEdge = 0
        topBoundary= int(self.rowLength-1)
        rightEdge = int(self.rowLength-1)
        bottomBoundary = int(len(self.tileList) - self.rowLength)
        edgeDistance = 0

        for tile in self.tileList:

            minedTileList = []

            if tileIndex > rightEdge:
                
                leftEdge = leftEdge + self.rowLength
                rightEdge = rightEdge + self.rowLength
                edgeDistance = rightEdge
            
            if tileIndex > topBoundary:

                tileAbove = int(tileIndex - self.rowLength)
                tile.adjacentTileDict['tileAbove'] = tileAbove
                minedTileList.append(self.tileList[int(tileAbove)].isMined)

                if tileIndex != rightEdge:
                    
                    tileAboveRight = int(tileIndex - self.rowLength + 1)
                    tile.adjacentTileDict['tileAboveRight'] = tileAboveRight
                    minedTileList.append(self.tileList[int(tileAboveRight)].isMined)
                
                if tileIndex != leftEdge:
                    
                    tileAboveLeft = int(tileIndex - self.rowLength - 1)
                    tile.adjacentTileDict['tileAboveLeft'] = tileAboveLeft
                    minedTileList.append(self.tileList[int(tileAboveLeft)].isMined)

            if tileIndex != rightEdge:
                
                tileRight = int(tileIndex + 1)
                tile.adjacentTileDict['tileRight'] = tileRight
                minedTileList.append(self.tileList[int(tileRight)].isMined)
            
            if tileIndex != leftEdge:
                
                tileLeft = int(tileIndex - 1)
                tile.adjacentTileDict['tileLeft'] = tileLeft
                minedTileList.append(self.tileList[int(tileLeft)].isMined)

            if tileIndex < bottomBoundary:
                
                tileBelow = int(tileIndex + self.rowLength)
                tile.adjacentTileDict['tileBelow'] = tileBelow
                minedTileList.append(self.tileList[int(tileBelow)].isMined)

                if tileIndex != rightEdge:
                    
                    tileBelowRight = int(tileIndex + self.rowLength + 1)
                    tile.adjacentTileDict['tileBelowRight'] = tileBelowRight
                    minedTileList.append(self.tileList[int(tileBelowRight)].isMined)

                if tileIndex != leftEdge:
                   
                    tileBelowLeft = int(tileIndex + self.rowLength - 1)
                    tile.adjacentTileDict['tileBelowLeft'] = tileBelowLeft
                    minedTileList.append(self.tileList[int(tileBelowLeft)].isMined)
        
            tile.surroundingMineCount = sum(minedTileList)

            tileIndex += 1
            edgeDistance -= 1

    def uncoverTiles(self, uncoverList):

        if uncoverList != []:

            for tile in uncoverList:
            
                if not tile.isMined and tile.isHidden and not tile.isMarked:

                    tile.isHidden = False
                    del self.tileDictionary[tile.label]

    def getTilesToUncover(self, tile, *args):

        adjacentTiles = tile.adjacentTileDict
      
        if tile.label not in self.tileDictionary.keys():

            return []

        if not args:

            uncoverList = []
            uncoverListCheck = []

        else:
            
            uncoverList = args[0]
            uncoverListCheck = args[1]
         
        uncoverList.append(tile)
        uncoverListCheck.append(tile.label)
        if tile.surroundingMineCount == 0:
            for adjacentTile in adjacentTiles:
          
                if adjacentTiles[adjacentTile] > -1:

                    uncoverTile = self.tileList[adjacentTiles[adjacentTile]]

                    if uncoverTile.surroundingMineCount == 0 and uncoverTile.label not in uncoverListCheck:
                   
                        uncoverList = self.getTilesToUncover(uncoverTile,uncoverList, uncoverListCheck)#, count)

                    else:

                        if uncoverTile not in uncoverList:

                            uncoverList.append(uncoverTile)
                            uncoverListCheck.append(uncoverTile.label)
                    
                else:

                    continue
    
        return uncoverList

        

            


    def printBoard(self):

        labelString = 'ABCDEFGHIJKLMNOPQRSTUVWX'

        rowLabelCount = 0
        columnLabelCount = 0
        
        tileCount = 0
        count = 1

        boardRow = ''

        for tile in self.tileList:

            tileCount += 1
    
            boardRow = boardRow  + str(tile)
            
            count += 1
            
            if tileCount == self.rowLength:

                print(boardRow)
                print ('\n')

                tileCount = 0
                boardRow = ''

        count = 1

    def setTileLabel(self):

        labelString = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()'

        rowLabelCount = 0
        columnLabelCount = 0
        
        tileCount = 0
        count = 1
        boardRow = ''

        for tile in self.tileList:

            tileLabel = ''
            tileCount += 1
            tile.label = labelString[rowLabelCount] + labelString[columnLabelCount]
            
            rowLabelCount += 1
            count += 1
            
            if tileCount == self.rowLength:
    
                tileCount = 0
                rowLabelCount = 0
                columnLabelCount += 1

        count = 1