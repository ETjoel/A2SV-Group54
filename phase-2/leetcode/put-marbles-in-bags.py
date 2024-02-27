class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        diffs = []
        for i in range(1,len(weights)):
            diffs.append(weights[i] + weights[i-1])
        diffs.sort()
        return sum(diffs[len(weights) - k: len(weights)]) - sum(diffs[:k-1])