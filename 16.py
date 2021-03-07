# https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        if len(nums2) > 0 :
            nums1[-len(nums2):] = nums2
        
        nums1.sort()
        return nums1
        