class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odds, evens = 0,0
        odds = n//2
        evens = n//2
        if n & 1 == 1: evens+=1
        return (pow(5, evens, 10**9+7) * pow(4, odds, 10**9+7)) % (10**9+7)