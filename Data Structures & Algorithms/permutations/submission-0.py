class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def f(l):
            if not len(l):return [[]]
            pm=f(l[1:])
            res=[]
            for p in pm:
                for i in range(len(p)+1):
                    pc=p[:]
                    pc.insert(i,l[0])
                    res.append(pc)
            return res
        return f(nums)