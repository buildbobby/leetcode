# solution to : https://leetcode.com/problems/shuffle-an-array

import random 
import copy

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        nums = self.nums.copy()
        for i in range(len(nums)):
            ind = random.randint(i,len(nums)-1)
            nums[i], nums[ind] = nums[ind], nums[i]

        return nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()