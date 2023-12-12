class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        counter = Counter(arr)
        for key, value in counter.items():
            if value > (n * 0.25):
                return key
        return 0