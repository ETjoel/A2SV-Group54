class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        wind = set()
        sum = res = 0
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and  nums[i] in wind:
                wind.remove(nums[j])
                sum -= nums[j]
                j+=1
            sum += nums[i]
            wind.add(nums[i])
            res = max(sum, res)
        return res
            
