# solution to : https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lproduct = [1]
        rproduct = [1]
        # how do you solve something like this in constant time 
        
        for num in nums:
            lproduct.append(num*lproduct[-1])
        
        for num in nums[::-1]:
            rproduct = [num*rproduct[0]] + rproduct
        
        lproduct = lproduct[:-1]
        rproduct = rproduct[1:]
        # how do you take care of all these things here on overall
        
        for ind in range(len(lproduct)):
            rproduct[ind] = lproduct[ind]*rproduct[ind]
        
        return rproduct
            