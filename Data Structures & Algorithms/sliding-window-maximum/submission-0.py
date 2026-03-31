class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        n=nums
        for i in range(k,len(n)+1):
            sub=n[i-k:i]
            res.append(max(sub))
        return res