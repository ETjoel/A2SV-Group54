class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        discard = set()
        for i in range(n):
            if nums[i] in discard:
                continue
            temp = set([i])
            j= (i + nums[i])%n
            while j not in temp and nums[i]*nums[j] > 0:
                temp.add(j)
                j = (j + nums[j])%n
            if j == i and len(temp) > 1:
                return True
            if nums[i]*nums[j] < 0:
                discard.update(temp)
        return False

            
            

