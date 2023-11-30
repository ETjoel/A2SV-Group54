class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for key in counter:
            values = counter[key]
            ans += (values - 1) / 2 * (values)
        return int(ans)