class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0] #just for ease
        currSum = 0

        for n in nums:
            currSum = max(currSum, 0) + n # if 0 is greater, just reset currSum to 0 and add that to n
            maxSum = max(maxSum, currSum)
        
        return maxSum
