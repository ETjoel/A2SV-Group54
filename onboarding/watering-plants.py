class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 1
        bucket = capacity
        bucket -= plants[0]
        for i in range(len(plants) - 1):
            temp = 1
            if bucket < plants[i + 1]:
                temp = (i + 1) * 2 + 1
                bucket = capacity
            steps += temp
            bucket -= plants[i + 1]
            print(temp)
        return steps

            