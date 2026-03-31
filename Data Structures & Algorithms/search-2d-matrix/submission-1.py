class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=matrix
        l,r=0,len(n)-1
        t=target
        m=-1
        found=False
        while l<=r:
            m=(l+r)//2
            if n[m][0]<=t and n[m][-1]>=t:
                found=True
                break
            if n[m][0]>t:
                r=m-1
            else:
                l=m+1
        if not found:return False
        n=n[m]
        print(n)
        l,r=0,len(n)-1
        while l<=r:
            m=(l+r)//2
            print(n[m])
            if n[m]==t:
                return True
            if n[m]>t:
                r=m-1
            else:
                l=m+1
        return False