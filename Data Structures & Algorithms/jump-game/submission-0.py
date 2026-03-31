class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp={}
        def f(i):
            if i in dp:return dp[i]
            if i==len(nums)-1:return True
            if nums[i]==0:return False

            end = min(len(nums), i + nums[i] + 1)
            for j in range(i+1,end):
                if f(j):
                    dp[i]=True
                    return True
            dp[i]=False
            return False
        return f(0)