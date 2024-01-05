class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        total = n * m
        walls = {(wall[0], wall[1]):True for wall in walls}
        _guards = {(guard[0], guard[1]):True for guard in guards}
        visited = {}
        for x, y in guards:
            for i in range(x-1, -1, -1):
                if (i, y) in walls or (i,y) in _guards : break
                visited[(i, y)] = True
            for i in range(x+1, m):
                if (i, y) in walls or (i,y) in _guards : break
                visited[(i, y)] = True
            for j in range(y-1, -1, -1):
                if (x, j) in walls or (x,j) in _guards: break
                visited[(x, j)] = True
            for j in range(y+1, n):
                if (x, j) in walls or (x,j) in _guards: break
                visited[(x, j)] = True
        return total - len(visited) - len(walls) - len(_guards)