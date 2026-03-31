class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr=[1]*len(nums)
        po=[1]*len(nums)
        for i in range(1,len(nums)):
            pr[i]=nums[i-1]*pr[i-1]
            j=-i-1
            po[j]=nums[j+1]*po[j+1]
        return [po[i]*pr[i] for i in range(len(nums))]