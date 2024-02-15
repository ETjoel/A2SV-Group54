class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        res,largestOdd = 0,0
        for value in counter.values():
            if value%2:
                largestOdd = max(largestOdd,value)
                res+=value-1
            else:
                res+=value
        return res+1 if largestOdd else res