class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        p=piles
        mk=max(p)
        def ep(k):
            return sum([math.ceil(i/k) for i in p])
        l,r=1,mk
        res=r
        while l<=r:
            m=(l+r)//2
            if ep(m)<=h:
                res=m
                r=m-1
            else:
                l=m+1
        return res