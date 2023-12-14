class UndergroundSystem:

    def __init__(self):
        self.dic = {}
        self.travels = defaultdict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dic[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time = t - self.dic[id][1]
        if (self.dic[id][0], stationName) in self.travels:
            self.travels[(self.dic[id][0], stationName)][0] += time
            self.travels[(self.dic[id][0], stationName)][1] += 1
        else:
            self.travels[ (self.dic[id][0], stationName)] = [time, 1]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
       
        return self.travels[(startStation, endStation)][0]/self.travels[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)