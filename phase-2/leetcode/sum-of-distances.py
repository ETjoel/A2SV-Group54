class Solution:
    def __init__(self,):
        self.res = []
    def helper(self, indexes: List[int], pref: List[int]) -> None:
        n = len(indexes)
        for i in range(n):
            right = pref[-1] - pref[i+1] - (n - i - 1)*indexes[i]
            left = (i* indexes[i]) - pref[i]
            self.res[indexes[i]] = left+right
    def distance(self, nums: List[int]) -> List[int]:
        self.res = [0 for _ in range(len(nums))]
        dic = {}
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]][0].append(i)
                dic[nums[i]][1].append(i + dic[nums[i]][1][-1])
            else:
                dic[nums[i]] = [[i],[0,i]]
        for key, values in dic.items():
            if len(values[0]) > 1:
                self.helper(values[0], values[1])
        return self.res
