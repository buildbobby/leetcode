# soln to : https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 1:
            return [nums] 
        else:
            permute_final = []
            permute_before = self.permute(nums[1:])
            
            for perm in permute_before:
                #print (perm)
                for i in range(len(perm)):
                    permute_final.append(perm[:i] + [nums[0]] + perm[i:])
                permute_final.append(perm + [nums[0]]) # edge case for last character of permutation
                    
        return permute_final