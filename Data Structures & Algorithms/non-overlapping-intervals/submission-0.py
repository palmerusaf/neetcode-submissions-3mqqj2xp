class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=intervals
        n.sort()
        res=0
        pe=n[0][1]
        for s,e in n[1:]:
            if s>=pe:
                pe=e
            else:
                res+=1
                pe=min(e,pe)
        return res