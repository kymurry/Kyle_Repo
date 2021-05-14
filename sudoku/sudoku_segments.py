
class SoSegment(object):

    def __init__(self):
        self.myList = []

    def append(self,element):
        self.myList.append(element)

    def __str__(self):
        if not self.myList:
            return ''
        else:
            return ''.join([str(x) for x in self.myList])

