class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        queue = deque([deck[0]])
        for i in range(1,len(deck)):
            top = queue.pop()
            queue.appendleft(top)
            queue.appendleft(deck[i])
        return queue