class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        maxim,total = nums[0],0
        for i in range(1, len(nums)):
            if nums[i] <= maxim:
                total += (maxim - nums[i])
            else:
                temp = min(nums[i], total)
                nums[i] -= temp
                total -= temp
                if total: total+=maxim
                elif nums[i] <= maxim:
                    total += (maxim - nums[i])
                else:
                    n = i+1
                    diff, rem = (abs(nums[i] - maxim))//n,  (abs(nums[i] - maxim)) % n
                    maxim +=diff + (1 if rem else 0)
                    total = (n - rem) if rem else 0
        return maxim
            



        return 0