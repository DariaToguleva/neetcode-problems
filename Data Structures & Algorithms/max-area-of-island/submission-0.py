class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxi = 0
        visited = set()

        def dfs(r, c, area):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    rU , cU = row + dr, col + dc
                    if (rU in range(rows) and cU in range(cols) 
                    and (rU, cU) not in visited and grid[rU][cU] == 1):
                        area += 1
                        q.append((rU, cU))
                        visited.add((rU, cU))  
            return area         

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = dfs(r, c, 1)
                    if area > maxi:
                        maxi = area        
        return maxi