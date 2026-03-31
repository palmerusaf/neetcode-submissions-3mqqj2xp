class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def f(i, pi, res):
            if i == len(nums):
                return res
            
            # skip
            skip = f(i + 1, pi, res)
            
            # take (only if valid)
            take = res
            if nums[i] > pi:
                take = f(i + 1, nums[i], res + 1)
            
            return max(skip, take)

        return f(0, float('-inf'), 0)