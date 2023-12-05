class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start == destination: return 0
        clock_wise , counter_clock_wise = 0, 0
        for i in range(min(start, destination), max(start, destination)):
            clock_wise += distance[i]
        counter_clock_wise = sum(distance) - clock_wise
        return min(clock_wise, counter_clock_wise)