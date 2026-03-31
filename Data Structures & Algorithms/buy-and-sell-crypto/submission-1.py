class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=prices
        l,r=0,1
        res=0
        while r<len(p):
            prof=p[r]-p[l]
            res=max(res,prof)
            if prof<0:
                l=r
            r+=1
        return res