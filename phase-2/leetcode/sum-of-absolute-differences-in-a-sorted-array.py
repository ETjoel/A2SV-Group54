class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total, n = sum(nums), len(nums)
        res = [total - nums[0]*n]
        prev, pref = 0, nums[0]
        for i in range(1, len(nums)):
            temp = total - pref
            temp -= nums[i] * (n - i)
            temp += prev + (nums[i] - nums[i-1])*i
            prev+=(nums[i] - nums[i-1])*i
            pref += nums[i]
            res.append(temp)
        return res