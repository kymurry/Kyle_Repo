
class SoSegment(object):

    def __init__(self):
        self.myList = []

    def append(self,element):
        self._myList.append(element)

    @property
    def myList(self):
        return [x.square_num for x in self._myList]

    @myList.setter
    def myList(self,container):
        self._myList = container

    def __str__(self):
        if not self.myList:
            return ''
        else:
            return ''.join([str(x) for x in self.myList])

