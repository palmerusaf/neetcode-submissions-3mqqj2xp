class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=nums
        n.sort()
        res=[]
        def f(i,s):
            if i ==len(n):
                res.append(s[:])
                return
            s.append(n[i])
            f(i+1,s)
            s.pop()
            while i+1<len(n) and n[i]==n[i+1]:
                i+=1
            f(i+1,s)
        f(0,[])
        return res
