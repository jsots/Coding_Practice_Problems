class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # Initialize the queue with the first position.
        q = deque([(0, 0, 1)]) # r, c, length
        visit = set((0, 0))
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        while q:
            r, c, length = q.popleft()
            # base case, you are out of bounds or at a blocked path
            if (min(r, c) < 0 or max(r, c) >= N or grid[r][c]):
                continue
            # other base case, you are at the destination
            if r == N - 1 and c == N - 1:
                return length
            for dr, dc in direct:
                if (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
            
        return -1