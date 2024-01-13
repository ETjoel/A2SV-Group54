class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        wind = res = j = 0
        for i in range(k):
            if s[i] in vowels: wind += 1
        res = wind
        for i in range(k, len(s)):
            wind += 1 if s[i] in vowels else 0
            wind -= 1 if s[i-k] in vowels else 0
            res = max(wind, res)
        return res
