class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        if not digits:return []
        np={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        d=digits
        sub=''
        def f(i):
            nonlocal sub
            if i>=len(d):
                res.append(sub[:])
                return
            for c in np[d[i]]:
                sub+=c
                f(i+1)
                sub=sub[:-1]
        f(0)
        return res