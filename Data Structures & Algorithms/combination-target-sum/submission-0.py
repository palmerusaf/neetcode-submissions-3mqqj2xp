class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        n=nums
        def f(si,pr,t):
            if not t:return res.append(pr[:])
            if t<0 or si>=len(n):return

            for i in range(si,len(n)):
                v=n[i]
                pr.append(v)
                f(i,pr,t-v)
                pr.pop()
        f(0,[],target)   
        return res