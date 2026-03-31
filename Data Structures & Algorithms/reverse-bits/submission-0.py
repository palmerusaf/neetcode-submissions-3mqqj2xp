class Solution:
    def reverseBits(self, n: int) -> int:
        n=bin(n)[2:][::-1]
        n=n+'0'*(32-len(n))
        n=int(n,2)
        print(n)
        return n