# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        ans = []
        if root:
            q.append(root)

        while q:
            right_side = None
            q_len = len(q)
            for i in range(q_len):
                node = q.popleft()
                if node:
                    right_side = node
                    # add the left first, that way the right side will always be the last thing added to the q.
                    q.append(node.left)
                    q.append(node.right)
            if right_side:
                ans.append(right_side.val)
        return ans