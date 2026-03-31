class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        t=target
        for i,n in enumerate(nums):
            d=t-n
            if d in mp:
                return [mp[d],i]
            mp[n]=i