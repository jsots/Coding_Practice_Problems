# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def sumOfLeft(root, cur_sum, is_right):
            # Base Case - im not anything
            if not root: 
                return 0

            # Base case - add the leaf if it is left
            
            if not root.left and not root.right:
                if not is_right:
                    cur_sum += root.val
                return cur_sum

            return sumOfLeft(root.left, cur_sum, False) + sumOfLeft(root.right, cur_sum, True)
        
        return sumOfLeft(root, 0, True)


