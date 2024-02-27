class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def helper(curr,visited):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for j in range(len(nums)):
                if nums[j] not in visited:
                    curr.append(nums[j])
                    visited.add(nums[j])
                    helper(curr, visited)
                    curr.pop()
                    visited.remove(nums[j])


        helper([],set())
        return res
