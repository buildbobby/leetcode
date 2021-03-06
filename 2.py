# soln to : https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        n  = len(s)-1
        for i in range(len(s)//2):
            s[i],s[n-i] = s[n-i], s[i]
        return s
