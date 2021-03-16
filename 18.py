# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort by the starting points
        # heuristic : ending curr > start prev interval , merge the two intervals 
        # NlgN + N 
        
        inter = sorted(intervals, key=lambda z : z[0])
        for ind in range(len(inter)-1):
            if inter[ind][1] >= inter[ind+1][0]:
                inter[ind+1] = ([min(inter[ind][0],inter[ind + 1][0]),max(inter[ind][1],inter[ind + 1][1])])
                inter[ind]  = None
        
        inter = [inter[i] for i in range(len(inter)) if inter[i] != None]
        return inter
                
            