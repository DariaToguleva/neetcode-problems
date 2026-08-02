class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        columns = len(grid[0])    
        visited = set()    
        islands = 0

        def dfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            
            while q:
                row, col = q.popleft()
                direct = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for dr, dc in direct:
                    rowU, colU = row + dr, col + dc
                    if (rowU in range(rows) and colU in range(columns) 
                    and grid[rowU][colU] == "1" and (rowU, colU) not in visited):
                        q.append((rowU, colU))
                        visited.add((rowU, colU))

        for r in range(rows):
                for c in range(columns):
                    if (grid[r][c] == "1" and (r, c) not in visited):
                        dfs(r, c)
                        islands += 1
        return islands                