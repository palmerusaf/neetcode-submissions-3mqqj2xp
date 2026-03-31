class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=numbers
        t=target
        l,r=0,len(n)-1
        while True:
            if n[l]+n[r]==t:
                return [l+1,r+1]
            if n[l]+n[r]>t:
                r-=1
            else:
                l+=1
