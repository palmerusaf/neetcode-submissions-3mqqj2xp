class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        pd=set()
        nd=set()
        res=[]
        board=[['.']*n for i in range(n)]
        def f(r):
            if r==n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):
                if c in col or (r+c) in pd or (r-c) in nd:
                    continue
                col.add(c)
                pd.add(r+c)
                nd.add(r-c)
                board[r][c]='Q'
                f(r+1)
                col.remove(c)
                pd.remove(r+c)
                nd.remove(r-c)
                board[r][c]='.'
        f(0)
        return res