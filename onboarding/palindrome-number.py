class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = abs(x)
        new = 0
        while y > 0:
            new = new * 10 + y % 10
            y //= 10
        print(new, abs(x))
        return x == new