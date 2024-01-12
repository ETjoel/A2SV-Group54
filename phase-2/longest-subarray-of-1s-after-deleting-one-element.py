class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # if sum(nums) == len(nums): return len(nums)-1
        wind = [0,0]
        res = 0
        j = 0
        for i in range(len(nums)):
            wind[nums[i]] += 1
            while wind[0] > 1 and j < len(nums):
                wind[nums[j]] -= 1
                j+=1
            res = max(res, wind[1] if wind[0] else wind[1]-1)
        return res


            