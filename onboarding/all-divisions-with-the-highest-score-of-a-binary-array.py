class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_once = sum(nums)
        ans = []
        left = 0
        for i in range(n):
            if i == 0:
                ans.append(total_once)
            else:
                left += nums[i-1]
                ans.append(total_once - left + i-left)
        ans.append(n - total_once)
        _max = max(ans)
        res = [i for i in range(n+1) if ans[i] == _max]
        return res
        
