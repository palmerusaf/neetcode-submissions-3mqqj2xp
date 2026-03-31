class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=prices
        if len(p)==1:
            return 0
        res=0
        for i in range(len(p)):
            for j in range(i+1,len(p),1):
                res=max(res,p[j]-p[i])
        return res