class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h=heights
        res=0
        for i in range(len(h)):
            for j in range(i,len(h)):
                w=j-i
                res=max(res,min(h[i],h[j])*w)
        return res