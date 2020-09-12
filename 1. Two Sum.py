class Solution:
    def twoSum(self, nums, target):
        output = []
        for i in range(len(nums)):
            element = target - nums[i]
            if element in nums:
                if i != nums.index(element):
                    output.append(i)
                    output.append(nums.index(element))
                    return output