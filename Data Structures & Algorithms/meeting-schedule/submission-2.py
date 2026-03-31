"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ii=intervals
        ii.sort(key=lambda i: i.start)
        for i in range(1,len(ii)):
            p=ii[i-1]
            n=ii[i]
            if p.end>n.start:
                return False
        return True