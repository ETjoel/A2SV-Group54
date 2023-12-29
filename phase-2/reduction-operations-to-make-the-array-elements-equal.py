class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        counter = Counter(nums)
        ans = 0
        for i, key in enumerate(sorted(counter.keys())):
            ans += i * counter[key]
        return ans
