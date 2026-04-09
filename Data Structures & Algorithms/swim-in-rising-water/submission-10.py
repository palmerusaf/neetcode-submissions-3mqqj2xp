class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        g=grid
        q=[(g[0][0],0,0)]
        v=set()
        while q:
            w,r,c=heapq.heappop(q)
            if (r,c) in v:continue
            v.add((r,c))
            if r==c==len(g)-1:return w

            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr,nc=r+dr,c+dc
                if nr<0 or nc<0 or nr>=len(g) or nc>=len(g) or (nr,nc) in v:continue
                heapq.heappush(q,(max(w,g[nr][nc]),nr,nc))