class MinStack:

    def __init__(self):
        self.l=[]

    def push(self, val: int) -> None:
        self.l.append({'v':val,'m':val if not len(self.l) else min(val,self.l[-1]['m'])})

    def pop(self) -> None:
        res=self.l.pop()

    def top(self) -> int:
        return self.l[-1]['v']

    def getMin(self) -> int:
        return self.l[-1]['m']
