class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        def f(i):
            if i>len(nums)-1:return res.append(sub[:])
            sub.append(nums[i])
            f(i+1)
            sub.pop()
            f(i+1)
        f(0)
        return res