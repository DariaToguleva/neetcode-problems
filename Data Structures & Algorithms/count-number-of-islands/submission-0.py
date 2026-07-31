class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        row, col = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def dfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                row1, col1 = q.popleft()
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    r1, c1 = row1 + dr, col1 + dc
                    if (r1 in range(row) and c1 in range(col) and 
                    (r1, c1) not in visit and grid[r1][c1] == "1"):
                        q.append((r1, c1))
                        visit.add((r1, c1))


        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    islands += 1
        return islands            


