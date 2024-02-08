class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        res = curr
        for i in range(1,len(nums)):
            if curr + nums[i] >= nums[i]:
                curr += nums[i]
            elif curr + nums[i] < nums[i]:
                curr = nums[i]
            res = max(curr, res)
        return res
            