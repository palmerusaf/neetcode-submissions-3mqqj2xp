class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(0,n+1):
            c=0
            while i:
                c+=i%2
                i=i//2
            res.append(c)
        return res