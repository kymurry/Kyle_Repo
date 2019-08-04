class SoTile(object):

    def __init__(self):
        self.test = True
        self.square_num = '0'

        self.adjacentTileDict = {'tileAbove':-1, 'tileAboveRight':-1, 'tileAboveLeft':-1, 'tileBelow':-1, 'tileBelowRight':-1, 'tileBelowLeft':-1, 'tileLeft':-1, 'tileRight':-1}

        self.uncovered = False

    def __str__(self):
        if self.test:
            return str(self.square_num)
        else:
            return ' ' + self.square_num if self.uncovered else '  '
