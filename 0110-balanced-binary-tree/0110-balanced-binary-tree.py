# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        self.balance = True
        def getHeight(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            l_height = getHeight(node.left)
            r_height = getHeight(node.right)
            self.balance = self.balance and (abs(l_height - r_height) < 2)
            return max(l_height,r_height) + 1
        getHeight(root)
        return self.balance
