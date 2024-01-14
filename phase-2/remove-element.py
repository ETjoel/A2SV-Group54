class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j, k = 0, nums.count(val)
        for i in range(len(nums)):
            if nums[i] == val:
                j=i
                while j < len(nums) and nums[j] == val: j+=1
                if j < len(nums) and nums[j]!=val:
                    nums[i], nums[j] = nums[j], nums[i]
        return len(nums)-nums.count(val)