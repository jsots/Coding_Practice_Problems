class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        if root.left or root.right:
            temp = root.left
            temp_2 = root.right
            root.left = temp_2
            root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

        