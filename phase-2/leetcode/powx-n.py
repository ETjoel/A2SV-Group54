import sys
sys.setrecursionlimit(5000)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def rec(x, n) -> float:
            if n == 0:
                return 1
            if n == 1:
                return x
            prev = rec(x, n//2)
            return x * prev * prev if n%2 else prev * prev
        if n >= 0:
            return rec(x, n)
        else:
            return (1/rec(x, abs(n)))
        #n == 10 
        