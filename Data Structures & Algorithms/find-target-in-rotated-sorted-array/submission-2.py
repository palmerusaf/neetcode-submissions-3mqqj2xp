class Solution:
    def search(self, nums: List[int], target: int) -> int:
        t=target
        n=nums
        l,r=0,len(n)-1
        while l<=r:
            m=(l+r)//2
            if n[m]==t:
                return m
            left_sorted=n[l]<=n[m]
            t_in_left=n[l]<=t<n[m]
            t_in_right=n[m]<=t<=n[r]
            if left_sorted:
                if t_in_left:
                    r=m-1
                else:
                    l=m+1
            else:
                if t_in_right:
                    l=m+1
                else:
                    r=m-1
        return -1