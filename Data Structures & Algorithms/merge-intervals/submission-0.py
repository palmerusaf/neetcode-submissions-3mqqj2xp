class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=intervals
        if len(n)<2:return n
        n.sort(key=lambda i:i[0])
        res=[n[0]]
        for s,e in n:
            pe=res[-1][1]
            if s<=pe:
                res[-1][1]=max(pe,e)
            else:
                res.append([s,e])
                
        return res