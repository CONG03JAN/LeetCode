# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        def helper(root, curSum):

            if not root:
                return False
            
            curSum += root.val

            if not root.left and not root.right:
                return curSum == sum
            
            return helper(root.left, curSum) or helper(root.right, curSum)

        if not root:
            return False
        return helper(root, 0)