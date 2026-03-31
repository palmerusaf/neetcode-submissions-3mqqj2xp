class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=nums
        if len(n)==1:
            return n[0]
        mi=len(n)//2
        l=n[:mi]
        r=n[mi:]
        return self.findMin(r) if r[-1]<=l[-1] else self.findMin(l)