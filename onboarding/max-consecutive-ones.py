class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        _max = 0
        ans = 0
        for num in nums:
            if num == 0:
                ans = max(ans, _max)
                _max = 0
            else:
                _max += 1
        ans = max(ans, _max)
        return ans