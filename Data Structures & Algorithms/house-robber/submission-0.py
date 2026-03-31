class Solution:
    def rob(self, nums: List[int]) -> int:
        nm1,nm2=0,0

        for n in nums:
            t=max(n+nm2,nm1)
            nm2=nm1
            nm1=t
        return nm1