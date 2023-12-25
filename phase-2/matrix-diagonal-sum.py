class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n= len(mat)
        primary, secondary = 0, 0
        for i in range(n):
            for j in range(n):
                primary += mat[i][j] if i - j == 0 else 0
                secondary += mat[i][j] if i + j == n-1 else 0
                primary -= mat[i][j] if i - j == 0 and  i + j == n - 1 else 0
        return primary + secondary