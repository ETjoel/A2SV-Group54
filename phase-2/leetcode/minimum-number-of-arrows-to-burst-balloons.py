class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        print(points)
        res,left, right = 1, points[0][0],points[0][1]
        for i in range(len(points)):
            if points[i][0] > right:
                left, right = points[i][0],points[i][1]
                res+=1
            else:
                left, right = points[i][0],min(points[i][1],right)
        return res
