# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.now = float("-inf")

    def isValidBST(self, root: TreeNode) -> bool:
        
        if not root:
            return True

        if self.isValidBST(root.left) == False:
            return False

        if self.now >= root.val:
            return False

        self.now = root.val

        if self.isValidBST(root.right) == False:
            return False

        return True

        