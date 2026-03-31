class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=nums
        t=target
        l,r=0,len(n)-1
        while(l<=r):
            m=(l+r)//2
            v=n[m]
            if v==t:
                return m
            if v<t:
                l=m+1
            else:
                r=m-1
        return -1