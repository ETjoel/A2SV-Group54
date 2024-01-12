class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        wind = sum(nums[0:k])
        res = wind/k
        for i in range(k, n):
            wind += nums[i]-nums[i-k]
            res = max(wind/k, res)
        return res