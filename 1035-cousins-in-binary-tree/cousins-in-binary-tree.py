# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        q = deque([(root, None)])

        while q:
            length = len(q)
            x_parent = None
            y_parent = None


            for i in range(length):
                node, parent = q.popleft()

                if node.val == x:
                    x_parent = parent

                if node.val == y:
                    y_parent = parent

                if node.left:
                    q.append([node.left, node])
                
                if node.right:
                    q.append([node.right, node])

            if x_parent is not None and y_parent is not None:
                return x_parent != y_parent

            if x_parent is not None or y_parent is not None:
                return False

                
        return False

                

                

            




        