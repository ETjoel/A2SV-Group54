class Solution:
    def sortColors(self, nums: List[int]) -> None:
        size = len(nums)
        temp = [0] * 3

        for i in range(len(nums)):
            temp[nums[i]] += 1

        k = 0
        for i in range(3):
            for j in range(temp[i]):
                nums[k] = i
                k += 1
        