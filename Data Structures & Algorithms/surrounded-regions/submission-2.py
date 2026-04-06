class Solution:
    def solve(self, board: List[List[str]]) -> None:
        b=board
        v={}
        def f(i,j):
            if i<0 or j<0 or i>=len(b) or j>=len(b[i]):
                return True
            if i in v and j in v[i]:
                return False
            if b[i][j]=='X':
                return False
            if not i in v:v[i]=set()
            v[i].add(j)
            res=(
                f(i+1,j) or
                f(i-1,j) or
                f(i,j+1) or
                f(i,j-1)
            )
            v[i].remove(j)
            return res
        for i in range(len(b)):
            for j in range(len(b[i])):
                if not f(i,j):
                    b[i][j]='X'
