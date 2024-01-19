class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res , j = float('INF'), 0
        wind = set()
        for i in range(len(cards)):
            if cards[i] in wind:
                while cards[i] in wind:
                    wind.remove(cards[j])
                    j+=1
                res = min(i + 2  - j, res)
            wind.add(cards[i])
        return res if res != float('INF') else -1