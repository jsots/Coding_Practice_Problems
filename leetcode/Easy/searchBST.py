# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None

        if val == root.val:
            return root
        elif val > root.val:
            return self.searchBST(root.right,val)
        else:
            return self.searchBST(root.left, val)

# My other solution - did all by myself and its v efficient

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None
            
            if node.val == val:
                return node
            
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
