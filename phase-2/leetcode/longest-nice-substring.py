class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def divideAndConquer(s):
            if s == '' or len(s) == 1:
                return ''

            counter = Counter(s)
            for i in range(len(s)):
                if not (s[i].upper() in counter and s[i].lower() in counter):
                    left = divideAndConquer(s[:i])
                    right = divideAndConquer(s[i+1:])
                    return left if len(left) >= len(right) else right
            return s
        return divideAndConquer(s)