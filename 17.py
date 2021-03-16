# https://leetcode.com/problems/add-binary/ # asked by FB a lot 
# lots of edge cases

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        len_min = min(len(a),len(b))
        
        b = b[::-1]
        a = a[::-1]
        
        if len(a) > len(b):
            minarr = b
            maxarr = a 
        else:
            maxarr = b
            minarr = a
        
        out = ''
        carry = 0
        
        for i in range(len_min):
            
            if int(minarr[i]) + int(maxarr[i]) + carry == 0:
                carry = 0
                out = '0' + out
            elif int(minarr[i]) + int(maxarr[i]) + carry == 1:
                carry = 0
                out = '1' + out
            elif int(minarr[i]) + int(maxarr[i]) + carry == 2:
                carry = 1 
                out = '0' + out
            else:
                carry = 1
                out = '1' + out
        
        
        for i in range(len(minarr),len(maxarr)):
            
            if ( carry + int(maxarr[i]) == 0):
                carry  = 0
                out = '0' + out
                
            elif (carry + int(maxarr[i]) == 1):
                carry  = 0
                out = '1' + out
            else:
                carry = 1
                out = '0' + out
            
                
        if carry == 1:
            out = '1' + out
                
        return out
        