"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
            n=intervals
            n=[[i.start,i.end] for i in n]
            type(n)
            n.sort()
            if len(n)<2:return True
            pe=n[0][1]
            for s,e in n[1:]:
                if s<pe:
                    return False
                else:
                    pe=e
            return True