class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=nums
        l,r=0,len(n)-1
        t=target
        while l<=r:
            m=(l+r)//2
            if n[m]==t:
                return m
            if n[m]>t:
                r=m-1
            else:
                l=m+1
        return -1