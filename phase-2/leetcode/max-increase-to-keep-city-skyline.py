class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxInRow, maxInCol = [0 for _ in range(n)], [0 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                maxInRow[i] = max(maxInRow[i], grid[i][j])
                maxInCol[j] = max(maxInCol[j], grid[i][j])
        res = 0
        for i in range(n):
            for j in range(n):
                res+=min(maxInRow[i], maxInCol[j]) - grid[i][j]
        return res
        