# https://leetcode.com/problems/maximum-depth-of-binary-tree
# think about the edge cases and problems in edge cases

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        elif root.right and root.left:
            depth = 1 + max(self.maxDepth(root.right),self.maxDepth(root.left))
        elif root.left:
            depth = 1 + self.maxDepth(root.left)
        elif root.right:
            depth = 1 + self.maxDepth(root.right)
        else:
            depth = 1
        return depth
            
