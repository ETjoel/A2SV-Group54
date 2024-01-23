class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        pref = 0
        if total - nums[0] == 0:
                return 0
        pref+=nums[0]
        for i in range(1, len(nums)):
            if total - nums[i] == 2*pref:
                return i
            pref+=nums[i]
        return -1