class Solution:
    def intersection(self, nums1, nums2):

      visited = {}

      result = []

      for num in nums1:
        visited[num] = num
        
      for num in nums2:       
        if num in visited:
            result.append(num)
            visited.pop(num)
            
      return result



- - - - - - - - - - - -Or - - - - - - - - - - - - - - - - - - - - -Simple Solution - - - - - - - - - - - -

class Solution:
    def intersection(self, nums1, nums2):
        return set(nums1) & set(nums2)