class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=prices
        l,r=0,1
        res=0
        while r<len(p):
            t=p[r]-p[l]
            if t>0:
                res=max(res,t)
            else:
                l=r
            r+=1
        return res