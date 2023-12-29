class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            nums = sorted(list(map(int, str(num*-1))), reverse= True)
            return -1*int(''.join([str(num) for num in nums]))
        else:
            nums = sorted(list(map(int, str(num))))
            for i in range(len(nums)):
                if nums[i] > 0 and nums[0] == 0:
                    nums[i], nums[0] = nums[0], nums[i]
                    break
            return int(''.join([str(num) for num in nums]))