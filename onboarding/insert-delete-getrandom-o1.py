class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.dic: 
            return False
        else:
            self.nums.append(val)
            self.dic[val] = len(self.nums) - 1
            return True

    def remove(self, val: int) -> bool:
        if val in self.dic:
            index = self.dic[val]
            if index == len(self.nums) - 1:
                self.nums.pop()
                self.dic.pop(val)
            else:
                self.nums[index] = self.nums[-1]
                self.dic[self.nums.pop()] = index
                self.dic.pop(val)

            return True
        else: return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()