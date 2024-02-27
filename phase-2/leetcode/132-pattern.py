class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mono_dec_stk = []
        minim = nums[0]
        for i in range(len(nums)):
            while mono_dec_stk and mono_dec_stk[-1][0] <= nums[i]:
                mono_dec_stk.pop()
            if mono_dec_stk and nums[i] > mono_dec_stk[-1][1]:
                return True

            mono_dec_stk.append((nums[i],minim))
            minim = min(minim, nums[i])
           
        return False