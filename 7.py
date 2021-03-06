class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # store the count of something 
        acc = nums[0] 
        for ind in range(1,len(nums)):
            acc = acc^nums[ind]
        return acc
            
        