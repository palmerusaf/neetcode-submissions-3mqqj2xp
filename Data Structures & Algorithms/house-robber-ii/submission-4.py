class Solution:
    def rob(self, nums: List[int]) -> int:
        n=nums
        if len(n)==1:return n[0]
        dp={}
        def f(i,iz):
            if i>=len(n):return 0
            if i ==len(n)-1 and iz:return 0
            res=max(n[i]+f(i+2,iz or i==0),f(i+1,iz))if i not in dp or iz not in dp[i] else dp[i][iz]
            if i not in dp:dp[i]={}
            dp[i][iz]=res
            return res
        return max(f(0,True),f(1,False))