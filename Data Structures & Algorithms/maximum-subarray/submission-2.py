class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=nums
        def f(l,r,c):
            if l==len(n) or r==len(n):return c
            return max(f(l+1,r+1,c),f(l,r+1,c),sum(n[l:r+1]))
        return f(0,0,-float('inf'))