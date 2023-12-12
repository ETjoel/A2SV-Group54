class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        print(n)
        return int((n / 2) * (n+1)) - sum(nums) 