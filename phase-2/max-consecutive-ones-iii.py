class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        wind = [0,0]
        j = res = 0
        for i in range(len(nums)):
            wind[nums[i]]+=1
            while j < len(nums) and wind[0] > k:
                wind[nums[j]]-=1
                j+=1
            print(wind)
            res = max(sum(wind), res)
        return res