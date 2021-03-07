import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_new = ""
        for ch in s:
            if (ch.isalnum()):
                s_new = s_new + ch   
        #print (s_new)
        n = len(s_new) - 1
        for i in range(len(s_new)//2):
            #print (s_new[i], s_new[n-i])
            if s_new[i] != s_new[n - i]:
                return False
        return True