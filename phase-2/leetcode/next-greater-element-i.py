class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stk = []
        for num in nums2:
            while len(stk) > 0 and stk[-1] < num: dic[stk.pop()] = num
            stk.append(num)
        ans = []
        for num in nums1:
            ans.append(dic.get(num, -1))
        return ans

            
