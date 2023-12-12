class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = sum(filter(lambda x: x % 2 == 0, nums))
        ans = []
        for val, index in queries:
            nums[index] += val
            if nums[index] % 2 == 0:
                total += val if val % 2 == 0 else nums[index]
            else:
                total -= nums[index] - val  if val%2==1 else 0
            ans.append(total)
        return ans
