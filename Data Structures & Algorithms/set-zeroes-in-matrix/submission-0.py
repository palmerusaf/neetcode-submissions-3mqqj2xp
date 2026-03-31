class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n=matrix
        c=[1]*len(n[0])
        r=[1]*len(n)
        for row in range(len(n)):
            for col in range(len(n[row])):
                if n[row][col]==0:
                    c[col]=0
                    r[row]=0
        for row in range(len(n)):
            for col in range(len(n[row])):
                if not r[row] or not c[col]:
                    n[row][col]=0

