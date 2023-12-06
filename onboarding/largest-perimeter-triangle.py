class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(2, len(nums)):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                ans = max(ans, nums[i - 2] + nums[i-1] + nums[i])
        return ans
