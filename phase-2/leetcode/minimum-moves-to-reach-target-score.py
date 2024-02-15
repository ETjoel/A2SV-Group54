class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        res = 0
        while target != 1:
            if not target % 2 and maxDoubles:
                target //=2
                maxDoubles-=1
                res+=1
            elif target % 2 and maxDoubles:
                target-=1
                res+=1
            elif not maxDoubles:
                res+=target-1
                target = 1
        return res