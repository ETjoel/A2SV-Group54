class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wind = set()
        j = res = 0
        for i in range(len(s)):
            while s[i] in wind:
                wind.remove(s[j])
                j+=1
            res = max(i-j+1, res)
            wind.add(s[i])
        return res