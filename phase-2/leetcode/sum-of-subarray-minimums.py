class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #monotonic stack implementations
        res = 0
        mono_inc_stk = []
        for i in range(len(arr)):
            while mono_inc_stk and mono_inc_stk[-1][0] > arr[i]:
                top = mono_inc_stk.pop()
                right = i - top[1]
                left = top[1] - mono_inc_stk[-1][1] if mono_inc_stk else top[1]+1
                res+=(left * right * top[0])
            mono_inc_stk.append((arr[i], i))
        while mono_inc_stk:
            top = mono_inc_stk.pop()
            right = len(arr) - top[1]
            left = top[1] - mono_inc_stk[-1][1] if mono_inc_stk else top[1]+1
            res+=(left * right * top[0])
        return res % (10**9 + 7)