class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        suduko = {(i, j): set() for i in range(3) for j in range(3)}
        rows , column = [set() for i in range(9)], [set() for i in range(9)]
        dots = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add((board[i][j]))
                    column[j].add(board[i][j])
                    suduko[(i//3,j//3)].add(board[i][j])
                else:
                    dots.append((i,j))
        def bactrack(ind):
            if ind >= len(dots):
                return True
            row, col = dots[ind]
            for i in range(1,10):
                i = str(i)
                if i not in rows[row] and i not in column[col] and i not in suduko[(row//3, col//3)]:
                    board[row][col] = str(i)
                    rows[row].add(str(i))
                    column[col].add(str(i))
                    suduko[(row//3, col//3)].add(str(i))
                    if bactrack(ind+1):
                        return True
                    else:
                        board[row][col] = '.'
                        rows[row].remove(str(i))
                        column[col].remove(str(i))
                        suduko[(row//3, col//3)].remove(str(i))
                
            return False
        bactrack(0)


            
            

        
                


        """
        Do not return anything, modify board in-place instead.
        """
        