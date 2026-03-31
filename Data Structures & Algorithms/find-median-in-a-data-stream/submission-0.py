class MedianFinder:

    def __init__(self):
        self.s,self.l=[],[]

    def addNum(self, num: int) -> None:
        def pus(v): heapq.heappush_max(self.s,v)
        def pos(): return heapq.heappop_max(self.s)
        def pul(v): heapq.heappush(self.l,v)
        def pol(): return heapq.heappop(self.l)
        pus(num)
        if self.l and self.s[0]>self.l[0]:
            pul(pos())
        while len(self.s)<len(self.l):
            pus(pol())
        while len(self.s)-len(self.l)>1:
            pul(pos())


        

    def findMedian(self) -> float:
        if len(self.s)==len(self.l):
            return (self.s[0]+self.l[0])/2
        else:
            return self.s[0]
        