class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums)-1):
            nums[i]+=i if nums[i] != 0 else 0
        target = len(nums) - 1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] >= target:
                target = i
        return target == 0