class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ik = len(cardPoints) - k
        total = sum(cardPoints)
        wind = sum(cardPoints[:ik])
        minimum = wind
        for i in range(ik, len(cardPoints)):
            wind += cardPoints[i] - cardPoints[i - ik]
            minimum = min(wind, minimum)
        return total - minimum