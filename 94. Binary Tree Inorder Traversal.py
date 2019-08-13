from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution_1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def helper(root):
            
            if not root: return

            # 左子树处理部分
            helper(root.left)

            # 根处理部分
            res.append(root.val)

            # 右子树处理部分
            helper(root.right)

        helper(root)
        return res

        
class Solution_2(object):
    def preorderTraversal(self, root):
        res = []

        stack = []
        p = root
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            res.append(p.val)
            p = p.right

        return res