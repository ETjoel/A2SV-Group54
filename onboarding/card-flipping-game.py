class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        nums = set(fronts + backs)
        for i in range(len(fronts)):
            if fronts[i] == backs[i] and fronts[i] in nums:
                nums.remove(fronts[i])
        if len(nums) == 0: return 0
        return nums.pop()