class Solution:
    def maxScore(self, s: str) -> int:
        s= list(map(int, s))
        total = sum(s)
        res = pref = 0
        for i in range(len(s)-1):
            pref += s[i]
            i + 1 - pref
            total - pref
            res = max(res,   total -  2*pref + i + 1)
        return res