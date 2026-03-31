class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        b=board
        rm,cm,clm={},{},{}

        for i in range(len(b)):
            for j in range(len(b[i])):
                el=b[i][j]
                if el == '.':
                    continue

                # check rows
                if i not in rm:
                    rm[i]=''
                if el in rm[i]:
                    return False
                else:
                    rm[i]+=el
                
                # check col
                if j not in cm:
                    cm[j]=''
                if el in cm[j]:
                    return False
                else:
                    cm[j]+=el

                # check cell
                ci=i//3
                cj=j//3
                if ci not in clm:
                    clm[ci]={}
                if cj not in clm[ci]:
                    clm[ci][cj]=''
                if el in clm[ci][cj]:
                    return False
                else:
                    clm[ci][cj]+=el
        return True