class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        m=set()
        for n in nums:
            if n in m:
                return n
            m.add(n)
            print(m)
