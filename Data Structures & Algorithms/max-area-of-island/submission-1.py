class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=grid
        res=0
        def f(i,j):
            nonlocal res
            if i>=len(n) or j>=len(n[i]):return 0
            if i<0 or j<0:return 0
            if not n[i][j]:return 0
            n[i][j]=0
            c=sum([1,
            f(i+1,j),
            f(i-1,j),
            f(i,j+1),
            f(i,j-1)])
            res=max(res,c)
            return c
        for i in range(len(n)):
            for j in range(len(n[i])):
                f(i,j)
        return res
            