class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        nums = nums[::-1]
        res  = total = 0
        i = 1
        while total < n:
            while nums and nums[-1] <= i: 
                total+=nums.pop()
                i=total
            if i > total:
                total+=i
                res+=1
                i=total
            i+=1
        return res