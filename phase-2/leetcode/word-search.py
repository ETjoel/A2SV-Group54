class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        def validDirection(row, col):
            if row < 0 or row >= n: return False
            if col < 0 or col >= m: return False
            return True
        def backtrack(s,visited,row, col,indx):
            # print(s, f'({row, col})', visited)
            if len(s) > len(word):
                return False
            if s == word:
                return True
            if (row,col) in visited or not validDirection(row,col):
                return False

            if board[row][col] == word[indx]:
                s += board[row][col]
                visited.add((row, col))
                i, j = row, col
                if backtrack(s,visited, i, j+1 ,indx+1):
                    return True
                elif backtrack(s,visited, i-1 , j ,indx+1):
                    return True
                elif backtrack(s,visited, i , j-1 ,indx+1):
                    return True
                elif backtrack(s,visited, i+1 , j ,indx+1):
                    return True
                visited.remove((row, col))

            else:
                return False
    
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if backtrack(word[0],set([(i,j)]), i, j+1 ,1):
                        return True
                    elif backtrack(word[0],set([(i,j)]), i-1 , j ,1):
                        return True
                    elif backtrack(word[0],set([(i,j)]), i , j-1 ,1):
                        return True
                    elif backtrack(word[0],set([(i,j)]), i+1 , j ,1):
                        return True
        return False


            