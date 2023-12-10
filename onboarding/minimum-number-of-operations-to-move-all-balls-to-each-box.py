class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # 2,4,5 | 1,3,4 | 0,2,3 | 1,1,2 | 2,0,1, | 3,1,0
        # 11      8       5       4       3          4
        ones = []
        for i, box in enumerate(boxes):
            if box == '1': ones.append(i)
        ans = []
        for i in range(len(boxes)):
            temp = 0
            for index in ones:
                temp += abs(i - index)
            ans.append(temp)
        return ans
