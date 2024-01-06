class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        suduko = {(i, j): set() for i in range(3) for j in range(3)}
        rows , column = [set() for i in range(9)], [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    print(num);print(suduko);print(rows);print(column)
                    if num in rows[i] or num in column[j] or num in suduko[(i//3,j//3)]: return 0
                    rows[i].add(num); column[j].add(num)
                    suduko[(i//3,j//3)].add(num)
        print(suduko);print(rows);print(column)
        return 1