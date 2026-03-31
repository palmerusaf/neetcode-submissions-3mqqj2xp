class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        mi,ma=1,1
        for n in nums:
            t=n*ma
            ma=max(t,n*mi,n)
            mi=min(t,n*mi,n)
            res=max(ma,res)
        return res