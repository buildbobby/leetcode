# solution to : https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort the array nlgn and then two pointers
        
        orderedmap = {}
        
        for ind, val in enumerate(nums):
            if val not in orderedmap:
                orderedmap[val] = [ind]
            else:
                orderedmap[val].append(ind)

        for num in nums:
            if (target - num) in orderedmap :
                if num!=target-num:
                    return [orderedmap[num][0],orderedmap[target-num][0]]
                elif len(orderedmap[num]) == 2:
                    return [orderedmap[num][0],orderedmap[target-num][1]]
            
        
        
        
        