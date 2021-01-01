class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        if len(nums) < 2:
            return nums
        
        result = []
        mid = int(len(nums)/2)
        
        y = Solution.sortArray(self, nums[:mid])
        z = Solution.sortArray(self, nums[mid:])
        
        while (len(y)>0) and (len(z)>0):
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        
        result += y
        result += z
        
        return result