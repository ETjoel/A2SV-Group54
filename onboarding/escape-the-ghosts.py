class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_turns = abs(target[0] - 0) + abs(target[1]  - 0)
        for ghost in ghosts:
            ghost_turns = abs(target[0] - ghost[0]) + abs(target[1] - ghost[1])
            if my_turns >= ghost_turns:
                return False
        return True