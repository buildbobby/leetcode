# https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:     
        if root == None:
            return [] 
        lvals, cvals, rvals = [],[],[]
        if root.left:
            lvals  = self.inorderTraversal(root.left)
        cvals  = [root.val]
        if root.right:
            rvals  = self.inorderTraversal(root.right)
        
        return lvals + cvals + rvals
        