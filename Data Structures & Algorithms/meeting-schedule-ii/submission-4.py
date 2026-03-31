"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n=intervals
        n=[[i.start,i.end] for i in n]
        sn=sorted([i for  i,_ in n])
        en=sorted([i for _,i in n])
        res,c=0,0
        s,e=0,0
        while s<len(n):
            if sn[s]<en[e]:
                s+=1
                c+=1
            else:
                e+=1
                c-=1
            res=max(res,c)
        return res