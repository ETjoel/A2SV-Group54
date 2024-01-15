class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        wind = Counter(blocks[:k])
        res = wind['W']
        for i in range(k, len(blocks)):
            wind[blocks[i]]+=1
            wind[blocks[i-k]]-=1
            res = min(res, wind['W'])
        return res