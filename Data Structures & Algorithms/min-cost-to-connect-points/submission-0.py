class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ps=points
        q=[[0,0]]
        res=0
        m={}
        v=set()

        while len(v)<len(ps):
            w,i=heapq.heappop(q)
            if i in v:continue
            res+=w
            v.add(i)
            for j in range(len(ps)):
                if i == j or j in v:continue
                xi,yi=ps[i]
                xj,yj=ps[j]
                d=abs(xi-xj)+abs(yi-yj)
                heapq.heappush(q,[d,j])

        return res