class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        v=set()
        g=grid
        for i in range(len(g)):
            for j in range(len(g[i])):
                if not g[i][j]:
                    q.append([i,j])
                    v.add((i,j))
        d=0
        def ar(i,j):
            if i<0 or j<0 or i>=len(g) or j>=len(g[i]) or g[i][j]==-1 or (i,j) in v:return
            v.add((i,j))
            q.append([i,j])
        while q:
            for i in range(len(q)):
                i,j=q.popleft()
                g[i][j]=d
                ar(i+1,j)
                ar(i-1,j)
                ar(i,j-1)
                ar(i,j+1)
            d+=1
                