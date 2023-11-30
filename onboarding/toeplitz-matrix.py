class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i, nums in enumerate(matrix):
            for j in range(len(nums)):
                if i > 0 and j > 0:
                    if nums[j] != matrix[i - 1][j - 1]:
                        return False
        return True