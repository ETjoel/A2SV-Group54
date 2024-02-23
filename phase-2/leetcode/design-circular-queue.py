class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.items = 0
        self.front = 0
        self.tail = -1
    def enQueue(self, value: int) -> bool:
        if self.items >= len(self.queue): return False
        self.queue[(self.tail+1) % len(self.queue)] = value
        self.tail = (self.tail+1) % len(self.queue)
        self.items+=1
        print(self.queue, self.front, self.tail, self.items)
        return True

        

    def deQueue(self) -> bool:
        if self.items <= 0:
            return False
        self.front = (self.front + 1) % len(self.queue)
        self.items-=1
        print(self.queue, self.front, self.tail, self.items)
        return True
    def Front(self) -> int:
        if self.items <= 0: return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.items <= 0: return -1
        return self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.items == 0

    def isFull(self) -> bool:
        return self.items == len(self.queue)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()