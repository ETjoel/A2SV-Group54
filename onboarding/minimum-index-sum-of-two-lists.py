class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        intersection = set(list1) & set(list2)
        least = float('inf')
        output = []
        for word in list(intersection):
            temp = list1.index(word) + list2.index(word)
            output.append([temp, word])
        output.sort()
        return [word[1] for word in output if word[0] == output[0][0]]