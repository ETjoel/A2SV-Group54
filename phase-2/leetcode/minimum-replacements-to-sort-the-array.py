class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        res = 0
        nums = nums[::-1]
        target = nums[0]
        for i in range(len(nums)):
            if target < nums[i]:
                spaces = math.ceil(nums[i]/target)
                res += spaces-1
                target = nums[i]//spaces
            else:
                target = nums[i]
        return res