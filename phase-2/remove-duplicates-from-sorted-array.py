class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[i] == nums[j]:
                j+=1
            if not j < len(nums): 
                return i+1
                break
            nums[i+1] = nums[j]
        