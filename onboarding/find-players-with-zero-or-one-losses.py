class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = [match[0] for match in matches]
        losers = [match[1] for match in matches]
        answer0 = list(set(winners) - set(losers))
        counter = Counter(losers)
        answer1 = []
        for key in counter:
            if counter[key] == 1:
                answer1.append(key)
        return [sorted(answer0), sorted(answer1)]