class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def predict(left, right, state):
            if left >= right:
                return state * nums[left]
            leftValue = nums[left] + state * predict(left+1, right, -state)
            rightValue = nums[right] + state * predict(left, right-1, -state)
            return state * max(leftValue, rightValue)
        print(predict(0, len(nums)-1, 1) )
        return predict(0, len(nums)-1, 1) >= 0
        