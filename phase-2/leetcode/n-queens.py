class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        matrix = [['.' for i in range(n)] for _ in range(n)]
        res = []
        def backtrack(pos, row):
            # print(matrix[0:4],pos['row'],row)
            if len(pos['row']) == n:
                temp = []
                for rows in matrix:
                    temp.append(''.join(rows))
                res.append(temp)
                return
            i = row
            for j in range(n):
                col = j
                rdiag,ldiag = i+j,  j - i
                if col not in pos['col'] and rdiag not in pos['rdiag'] and ldiag not in pos['ldiag']:
                    matrix[i][j] = 'Q'
                    pos['row'].add(i)
                    pos['col'].add(j)
                    pos['rdiag'].add(i+j)
                    pos['ldiag'].add(j-i)
                    backtrack(pos,row+1)
                    matrix[i][j] = '.'
                    pos['row'].remove(i)
                    pos['col'].remove(j)
                    pos['rdiag'].remove(i+j)
                    pos['ldiag'].remove(j-i)
            return 
        backtrack({'row':set(),'col':set(),'rdiag':set(),'ldiag':set()},0)
        return res
            

           
            