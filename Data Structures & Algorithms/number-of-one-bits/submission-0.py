class Solution:
    def hammingWeight(self, n: int) -> int:
      b=32
      res=0
      for _ in range(b):
        res+=n%2
        n=n//2
      return res