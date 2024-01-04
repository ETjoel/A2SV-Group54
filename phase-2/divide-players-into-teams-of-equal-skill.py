class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res,target,j = 0,skill[0]+skill[len(skill)-1],len(skill)-1
        for i in range(len(skill)):
            if i >= j: break
            if skill[i]+skill[j]!=target:return -1
            res+=skill[i]*skill[j]
            j-=1
        return res
