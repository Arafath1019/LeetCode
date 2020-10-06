#### Using Kadane's Algorithm


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return nums[0]


        sum1 = 0
        best = nums[0]
        for i in range(len(nums)):
            sum1 = max(nums[i], nums[i] + sum1)
            best = max(best, sum1)
        return best