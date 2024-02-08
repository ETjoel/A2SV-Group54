class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        all_nums = len(set(nums))
        wind = {}
        res = j = 0
        for i in range(len(nums)):
            wind[nums[i]] = wind.get(nums[i], 0) + 1
            while len(wind) == all_nums:
                res += len(nums) - i
                wind[nums[j]] -= 1
                if wind[nums[j]] < 1: del wind[nums[j]]
                j +=1
        return res