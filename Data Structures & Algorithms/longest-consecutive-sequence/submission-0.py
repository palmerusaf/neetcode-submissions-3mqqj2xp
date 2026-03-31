class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        res=0
        for n in nums:
            ln=0
            while n+ln in st:
                ln+=1
            res=max(res,ln)
        return res