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