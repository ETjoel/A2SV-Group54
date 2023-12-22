class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans, n, m = set(), len(strs[0]), len(strs)
        for i in range(1, m):
            for j in range(n):
                if ord(strs[i][j]) < ord(strs[i-1][j]):
                    ans.add(j)
        return len(ans)