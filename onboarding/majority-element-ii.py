class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        n = len(nums)
        return [key for key in counter if counter[key] > n//3 ]