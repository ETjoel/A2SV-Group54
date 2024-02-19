class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        target = tickets[k]
        for i in range(len(tickets)):
            if i <= k:
                res+=target if tickets[i]>=target else tickets[i]
            else:
                res+= tickets[i] if tickets[i]<target else target-1
          
        return res