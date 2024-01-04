class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res,i,j = 0,0,len(nums)-1
        while i < j:
            if nums[i]+nums[j]==k:
                res+=1;j-=1;i+=1
            elif nums[i]+nums[j]>k:j-=1
            else:i+=1
        return res
        
