## solution to : https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        else:
            p_combs = self.subsets(nums[1:])
            f_combs = []
            for comb in p_combs:
                f_combs = f_combs + [[nums[0]] + comb] + [comb]
            return f_combs
            