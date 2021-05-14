class SoTile(object):

    def __init__(self):
        self.test = True
        self.square_num = 0
        self.label = None

        self.tile_elements = {'tileRow':None, 'tileColumn':None, 'tileSquare':None}

        self.uncovered = False

    def __str__(self):
        if self.test:
            return str(self.square_num)# + ' ' + self.tile_elements['tileRow'] + ' ' +  self.tile_elements['tileColumn'] + ' ' + self.tile_elements['tileSquare']
        else:
            return ' ' + self.square_num if self.uncovered else '  '
