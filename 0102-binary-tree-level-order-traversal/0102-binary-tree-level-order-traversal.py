# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        res = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    level.append(curr.val)
                    if curr.left:                
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
            if len(level) > 0:
                res.append(level)
        return res