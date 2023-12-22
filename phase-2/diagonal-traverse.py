class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m , n = len(mat), len(mat[0])
        res = [[] for _ in range(m+n-1)]
        for i in range(m):
            for j in range(n):
                res[i+j].append(mat[i][j])
        ans = []
        for i, nums in enumerate(res):
            if i % 2 == 0:
                ans += reversed(nums)
            else:
                ans += nums
        return ans