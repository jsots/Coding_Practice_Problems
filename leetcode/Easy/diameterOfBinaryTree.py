class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        depth = 0
        left = self.find_longest_path(root.left, depth)
        right = self.find_longest_path(root.right, depth)

        return left + right
    
    def find_longest_path(self, root, depth):
        if not root:
            return depth
        
        depth = 1 + max(self.find_longest_path(root.left, depth), self.find_longest_path(root.right, depth))
        return depth