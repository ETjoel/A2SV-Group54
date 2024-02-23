class Solution:
    def trap(self, height: List[int]) -> int:
        mon_dec_stk = []
        res = 0
        for i in range(len(height)):
            while mon_dec_stk and mon_dec_stk[-1][0] < height[i]:
               block = mon_dec_stk.pop()
               if mon_dec_stk:
                   leftBound, index = mon_dec_stk[-1]
                   minBound = min(height[i], leftBound)
                   res+=(i - index - 1) * (minBound - block[0])
            mon_dec_stk.append((height[i], i))
        return res