class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000
        }
        total, j, n = 0, 1, len(s)
        while j < n:
            if values[s[j]] > values[s[j - 1]]:
                total += values[s[j]] - values[s[j - 1]]
                j += 1
            else:
                total += values[s[j - 1]]
            j += 1
        if values[s[n-1]]  <= values[s[n - 2]]: total += values[s[n - 1]]
        return total