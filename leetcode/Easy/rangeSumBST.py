# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = []
        def dfs(node):
            if not node:
                return 0

            dfs(node.left)
            
            ans.append(node.val)
            
            dfs(node.right)

            return ans

        dfs(root)

        cur_sum = 0
        for num in ans:
            if num >= low and num <= high:
                cur_sum += num
        
        return cur_sum

