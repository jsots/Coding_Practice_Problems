class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        ans = []
        if root:
            q.append(root)

        while q:
            curr = q.popleft()
            ans.append(curr.val)
            if curr.right:
                q.append(curr.right)
        
        return ans