# https://leetcode.com/problems/to-lower-case

class Solution:
    def toLowerCase(self, str: str) -> str:
        out = ''
        for s in str:
            out = out + s.lower()
        return out