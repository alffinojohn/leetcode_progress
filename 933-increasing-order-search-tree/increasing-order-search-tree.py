# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        def dfs(node):

            if not node:
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)

        dummy = TreeNode(0)
        curr = dummy

        for val in res:
            curr.right = TreeNode(val)
            curr = curr.right

        return dummy.right


            