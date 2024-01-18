class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count_odd = res = 0
        count = j = 0
        for num in nums:
            if num % 2 == 1:
                count_odd+=1
                count = 0
            while count_odd == k:
                if nums[j] % 2 == 1:
                    count_odd-=1
                j+=1
                count+=1
            res+=count
        return res