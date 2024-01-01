class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse= True)
        ans, j = 0, 0
        for i in range(len(processorTime)):
            ans = max(processorTime[i] + max(tasks[i*4:i*4+4]), ans)
        return ans
