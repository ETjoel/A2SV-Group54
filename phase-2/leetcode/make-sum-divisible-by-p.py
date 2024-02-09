class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        target = sum(nums) % p
        pref_dic,n = {},len(nums)
        pref,res = 0,n

        if target==0: return 0
    
        for i,num in enumerate(nums):
            pref = (pref+num)%p
            if (pref-target)%p in pref_dic:
                res = min(res,i-pref_dic.get((pref-target)%p))
            elif pref % p == target:
                res = min(res,i+1)
            pref_dic[pref] = i
        return res if res < n else -1