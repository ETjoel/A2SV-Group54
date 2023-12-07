class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        j = n
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[j])
            j += 1
        return output
            
