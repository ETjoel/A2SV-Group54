class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        pref = [0]*102
        for num in nums: pref[num] += 1
        prev = 0
        for i in range(102):
            pref[i] += pref[i-1]
        pref[-1] = 0
        return [pref[num-1] for num in nums]
