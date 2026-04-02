class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        sub=[]
        def f(i):
            if i >=len(s):
                res.append(sub[:])
                return
            for j in range(i,len(s)):
                ss=s[i:j+1]
                if ss==ss[::-1]:
                    sub.append(ss)
                    f(j+1)
                    sub.pop()
        f(0)
        return res