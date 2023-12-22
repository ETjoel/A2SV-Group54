class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        pref,m,n = [], len(grid), len(grid[0])
        for i in range(m):
            row, pr = [], 0
            for j in range(n):
                temp = pr + grid[i][j]
                temp += pref[i-1][j] if i >= 1 else 0
                pr += grid[i][j]
                row.append(temp)
            pref.append(row)
        print(pref)
        ans = -1
        for i in range(2,m):
            for j in range(2,n):
                temp = pref[i][j]
                temp -= pref[i][j-3] if j >= 3 else 0
                temp -= pref[i - 3][j] if i >= 3 else 0
                temp -= (grid[i-1][j] + grid[i-1][j-2])
                temp += pref[i-3][j-3] if i >= 3 and j >= 3 else 0
                ans = max(temp, ans)
        return ans

        return 0

        