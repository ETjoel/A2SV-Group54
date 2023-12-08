class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative, positive = [], []
        for num in nums:
            if num > 0: positive.append(num)
            if num < 0: negative.append(num)
        ans = []
        for i in range(len(nums) // 2):
            ans.append(positive[i])
            ans.append(negative[i])
        return ans