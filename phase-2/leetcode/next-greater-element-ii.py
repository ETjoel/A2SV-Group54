class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mono_dec_stk = []
        res = [-1 for _ in range(len(nums))]
        for i in range(len(nums)):
            while mono_dec_stk and nums[i] > mono_dec_stk[-1][0]:
                top = mono_dec_stk.pop()
                res[top[1]] = nums[i]
            mono_dec_stk.append((nums[i],i))
        for num in nums:
             while mono_dec_stk and num > mono_dec_stk[-1][0]:
                top = mono_dec_stk.pop()
                res[top[1]] = num
        
        return res