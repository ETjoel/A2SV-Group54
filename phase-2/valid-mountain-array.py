class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        if arr[0] > arr[1]: return False
        uphill = True
        for i in range(1, len(arr)):
            if uphill:
                if arr[i] < arr[i - 1]:
                    uphill = False
                elif arr[i] == arr[i-1]: return False
            else:
                if arr[i] >= arr[i - 1]: return False
        if uphill: return False
        return True