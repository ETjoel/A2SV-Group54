class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        count, j, ans = len(piles)//3, len(piles) - 2, 0
        while count > 0:
            ans += piles[j]; j -= 2; count -= 1
        return ans