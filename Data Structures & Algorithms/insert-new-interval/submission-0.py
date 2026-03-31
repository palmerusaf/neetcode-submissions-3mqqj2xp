class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n=intervals
        nn=newInterval
        res=[]
        for i in range(len(n)):
            if nn[1]<n[i][0]:
                res.append(nn)
                return res + n[i:]
            elif nn[0]>n[i][1]:
                res.append(n[i])
            else:
                nn=[min(nn[0],n[i][0]),max(nn[1],n[i][1])]
        res.append(nn)
        return res