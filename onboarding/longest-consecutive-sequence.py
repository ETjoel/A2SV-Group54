class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # chain = {}
        # for num in nums:
        #     if num + 1 in chain:
        #         chain[num] = chain[num+1]+1
        #     elif num not in chain:
        #         chain[num] = 1
        #     temp = num
        #     while temp - 1 in chain:
        #         chain[temp-1] = chain[temp] + 1
        #         temp -= 1
        #     print(chain)
        # return max(chain.values())
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        dic = {num : 1 for num in nums}
        visited = {}
        i = 0
        while i < len(nums):
            count = 0
            temp = nums[i] - 1
            while temp in dic and temp not in visited:
                count += dic[temp]
                visited[temp] = 1
                temp -= 1
            dic[nums[i]] += count
            i += 1
        
        return max(dic.values())
            