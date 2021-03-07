# https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # determining some kind of an anagram 
        sl = sorted(list(s))
        tl = sorted(list(t))
        
        if sl == tl:
            return True
        else:
            return False
            