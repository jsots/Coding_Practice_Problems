# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hasPathSum2(root, targetSum, curr_sum):
            if not root:
                return False

            curr_sum += root.val
            
            if not root.left and not root.right:
                return curr_sum == targetSum

            return hasPathSum2(root.left, targetSum, curr_sum) or hasPathSum2(root.right, targetSum, curr_sum)
        
        return hasPathSum2(root, targetSum, 0)


# sort of alt solution. basically the same thing

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curr_sum):
            if not node:
                return False
            
            curr_sum += node.val

            if not node.left and not node.right:
                return curr_sum == targetSum
            
            return (dfs(node.left, curr_sum) or dfs(node.right, curr_sum))
        
        return dfs(root, 0)
