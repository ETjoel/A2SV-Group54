class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        sum_dic = {nums[0]:1}
        if nums[0] == goal: res +=1
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            if nums[i] == goal:
                res += 1
            if nums[i] - goal in sum_dic:
                res += sum_dic[nums[i] - goal]
            sum_dic[nums[i]] = sum_dic.get(nums[i], 0) + 1
        print(sum_dic)
        return res
            
        

