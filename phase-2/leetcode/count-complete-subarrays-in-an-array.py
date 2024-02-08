class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        all_nums = set(nums)
        res = 0
        for i in range(len(nums)):
            wind = set()
            for j in range(i, len(nums)):
                wind.add(nums[j])
                if wind == all_nums:
                    res += len(nums) - j
                    break
        return res