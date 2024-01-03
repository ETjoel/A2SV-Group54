class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        j, ans = len(nums)-1, 0
        for i in range(len(nums)):
            if nums[i] + nums[j] >= target:
                while j > i and nums[i] + nums[j] >= target: j-=1
                if nums[i] + nums[j] < target:
                    ans += j - i
            elif nums[i] + nums[j] < target:
                ans += j - i
        return ans
