# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        seq_1 = []
        seq_2 = []

        def dfs(node, one_or_two):
            one = one_or_two
            if not node:
                return
            
            if not node.left and not node.right and one:
                seq_1.append(node.val)
            if not node.left and not node.right and not one:
                seq_2.append(node.val)
            
            dfs(node.left, one_or_two)
            dfs(node.right, one_or_two)
            if one:
                return seq_1
            else:
                return seq_2
        
        dfs(root1, True)
        dfs(root2, False)

        print(seq_1, seq_2)

        return seq_1 == seq_2