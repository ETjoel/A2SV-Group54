class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        wind = {}
        j = res = 0
        for i in range(len(fruits)):
            wind[fruits[i]] = wind.get(fruits[i], 0) + 1
            while len(wind) > 2:
                wind[fruits[j]] -= 1
                if wind[fruits[j]] <= 0: del wind[fruits[j]]
                j+=1
            res = max(res, sum(wind.values()))
        return res