class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i + 1
                while j < len(nums) and nums[j] == 0: 
                    j+=1
                if j == len(nums): break
                nums[i], nums[j] = nums[j], 0
            
        """
        Do not return anything, modify nums in-place instead.
        """
        