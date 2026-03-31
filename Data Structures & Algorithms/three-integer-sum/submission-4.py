class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=nums
        res=[]
        for i in range(len(n)):
            if n[i]>0:
                break
            l,r=i+1,len(n)-1
            while l < r:
                trip=[n[i],n[l],n[r]]
                trip.sort()
                sm=sum(trip)
                if sm > 0:
                    r-=1
                elif sm < 0:
                    l+=1
                else:
                    if trip not in res:
                        res.append(trip)
                    l+=1
                    r-=1

        return res