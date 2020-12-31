class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        for i in range(1, len(nums2)+1):
            nums1[len(nums1)-i] = nums2[len(nums2)-i]
        
        
        for i in range(len(nums1)):
            for j in range(len(nums1)-i-1):
                if nums1[j] > nums1[j+1]:
                    nums1[j], nums1[j+1] = nums1[j+1], nums1[j]
        
        return nums1
        