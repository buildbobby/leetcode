# solution to : https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_hash = {}
        for num in nums:
            if num not in num_hash:
                num_hash[num] = 0
            else:
                return True
        return False
            