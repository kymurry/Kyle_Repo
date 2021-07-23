import inspect

class SoSegment(object):

    def __init__(self):
        self.myList = ()

    def append(self,element):
        self._myList.append(element)

    @property
    def myList(self):
        #import pdb;pdb.set_trace()
        return [x.square_num for x in self._myList]
    
    def get_sotiles(self,index):
        return [x for x in self._myList] if index == -1 else self._myList[index]

    @myList.setter
    def myList(self,*args):
        g = args
        CurFrame = inspect.currentframe()
        CallFrame = inspect.getouterframes(CurFrame, 2)
        CallFunc = CallFrame[1][3]
        #import pdb;pdb.set_trace()
        if not args[0] and CallFunc == '__init__':
            self._myList = []
        elif isinstance(args[0][0],int):
            self._myList[args[0][0]].square_num = args[0][1]
        else:
            for tup in args[0]:
                self._myList[tup[0]].square_num = tup[1]

    def clear_segment(self,index=None):
        if index == None:
            for sotile in self._myList:
                sotile.square_num = 0
        else:
            for num in index:
                self._myList[num].square_num = 0

    def __str__(self):
        if not self._myList:
            return ''
        else:
            return ''.join([str(x) for x in self._myList])

