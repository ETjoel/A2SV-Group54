class RecentCounter:

    def __init__(self):
        self.counter =[]
        self.left = 0
    def ping(self, t: int) -> int:
        self.counter.append(t)
        while self.left < len(self.counter) and  self.counter[self.left] < min(t,t-3000):
            self.left+=1
        return len(self.counter) - self.left
        
        

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)