class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        combined = [[indices[i], s[i]] for i in range(len(s))]
        combined.sort()
        return ''.join([combined[i][1] for i in range(len(s))])