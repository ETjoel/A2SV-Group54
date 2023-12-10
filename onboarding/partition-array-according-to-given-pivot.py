class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        target = []
        for num in nums:
            if num < pivot: left.append(num)
            elif num == pivot: target.append(num)
            else: right.append(num)
        return left + target + right