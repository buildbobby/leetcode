class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == '' and needle == '':
            return 0
        elif len(haystack) < len(needle):
            return -1 
        
        for ind in range(len(haystack)-len(needle)+1):
            flag = 1
            for nind in range(len(needle)):
                if haystack[ind+nind]  != needle[nind]:
                    flag = 0
                    break
            if (flag == 1):
                return ind
        
        return -1 