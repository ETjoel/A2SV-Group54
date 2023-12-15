class ATM:

    def __init__(self):
        self.notes = [0]*5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.notes[i] += banknotesCount[i]
        print(self.notes)
    def withdraw(self, amount: int) -> List[int]:
        dic = {0:20, 1:50, 2:100,3:200, 4:500}
        withdrew = [0]*5
        for i in range(4, -1, -1):
            if self.notes[i] and amount >= dic[i]:
                count, remainder = divmod(amount, dic[i])
                temp = min(count, self.notes[i])
                count -= temp
                amount -= temp * dic[i]
                withdrew[i] = temp
      
        if amount: 
            return [-1]
        if not amount:
            for i in range(5):
                self.notes[i] -= withdrew[i]
        print(self.notes, amount)
        return withdrew
            
            


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)