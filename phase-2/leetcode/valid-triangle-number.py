class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        res= 0
        for i in range(len(nums) - 2):
            left, right= i+1, len(nums)-1
            while left < right:
                if nums[i] < nums[left]+nums[right]:
                    res+=right-left
                    left+=1
                else:
                    right-=1
        return res
            

        