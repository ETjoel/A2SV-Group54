class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        total, _max, ans = 0, 0, 0
        for i in range(len(flips)):
            total += flips[i]
            _max = max(_max, flips[i])
            if total == int((_max/2) * (1 + _max)):
                ans += 1
        return ans