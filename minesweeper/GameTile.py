class GameTile(object):



    def __init__(self):

        self.isMined = False
        self.isMarked = False
        self.isHidden = True
        self.label = ''
        self.surroundingMineCount = 0

        self.adjacentTileDict = {'tileAbove':-1, 'tileAboveRight':-1, 'tileAboveLeft':-1, 'tileBelow':-1, 'tileBelowRight':-1, 'tileBelowLeft':-1, 'tileLeft':-1, 'tileRight':-1}

        self.gameOver = False

    def __str__(self) :

        if self.isMarked:

            return ' ' +  '(' + self.label + ')'

        elif not self.isHidden:

            return '  ' + str(self.surroundingMineCount) + '  '

        elif not self.isHidden and self.isMined:

            return '  *  '

        elif self.gameOver and not self.isMined:

            return '  ' + str(self.surroundingMineCount) + '  '

        else:

            return '  ' + self.label + ' '