class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b=nums1,nums2
        t=len(a)+len(b)
        h=t//2
        if len(b)<len(a):
            a,b=b,a

        l,r=0,len(a)-1
        while True:
           i=(l+r)//2
           j=h-i-2

           al=a[i] if i>=0 else -float('inf')
           ar=a[i+1] if i+1<len(a) else float('inf')
           bl=b[j] if j>=0 else -float('inf')
           br=b[j+1] if j+1<len(b) else float('inf')

           if al<=br and bl<=ar:
                if t%2:
                    return min(ar,br)
                else:
                    return (max(al,bl)+min(ar,br)) / 2
           elif al>br:
                r=i-1
           else:
                l=i+1
