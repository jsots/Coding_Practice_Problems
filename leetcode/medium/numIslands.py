class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visit = set()

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or (r, c) in visit or grid[r][c] != "1":
                return
            visit.add((r , c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1
        
        return islands


# same as above but changing it to v for visit instead of making a hash map

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or grid[r][c] != "1":
                return
            grid[r][c] = "v"
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c):
                    dfs(r, c)
                    islands += 1
        
        return islands