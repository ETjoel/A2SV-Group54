class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        store = {5:0,10:0}
        change = 0
        for i in range(len(bills)):
            store[bills[i]] = store.get(bills[i],0)+1
            change = bills[i] - 5
            if change == 15 and store[10] and store[5]:
                store[10]-=1;store[5]-=1
            elif change ==15 and store[5]>= 3:
                store[5]-=3
            elif change ==15:
                return False
            elif change == 5 and store[5]:
                store[5]-=1
            elif change==5:
                return False
        return True


