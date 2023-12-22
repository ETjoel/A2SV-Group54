class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for img in image:
            temp = img[::-1]
            for i in range(len(temp)):
                temp[i] = 1-temp[i]
            res.append(temp)
        return res
            

