#[934. Shortest Bridge](https://leetcode.com/problems/shortest-bridge/description/) 
+ `Medium`

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.


+ Example 1:

```
Input: grid = [[0,1],[1,0]]
Output: 1
```

+ Example 2:

```
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
```

+ Example 3:

```
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
```


+ Constraints:

```
n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
```

# Solution:
```python {.line-numbers}
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        find_island = False
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    continue

                island = self.findIsland_DFS(r, c, grid, N)
                find_island = True
                break
            if find_island:
                break

        return self.computeBridgeLength(island, grid, N)

    def isValid(self, r, c, N):
        return False if (r < 0 or c < 0 or r >= N or c >= N) else True

    def findIsland_DFS(self, r, c, grid, N):
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[0] * N for _ in range(N)]

        island = []
        visited[r][c], stack = 1, [(r, c)]
        while len(stack) > 0:
            tr, tc = stack.pop()
            island.append((tr, tc))
            for nei in neighbors:
                tr_n, tc_n = tr + nei[0], tc + nei[1]
                if not self.isValid(tr_n, tc_n, N) or visited[tr_n][tc_n]:
                    continue

                visited[tr_n][tc_n] = 1
                if grid[tr_n][tc_n] == 1:
                    stack.append((tr_n, tc_n))

        return island

    def computeBridgeLength(self, island, grid, N):
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[0] * N for _ in range(N)]
        for r, c in island:
            visited[r][c] = 1

        dist = 0
        stack = island
        while len(stack) > 0:
            new_stack = []
            for r, c in stack:
                for nei in neighbors:
                    nr, nc = r + nei[0], c + nei[1]
                    if not self.isValid(nr, nc, N) or visited[nr][nc]:
                        continue

                    visited[nr][nc] = 1
                    if grid[nr][nc] == 1:
                        return dist
                    else:
                        new_stack.append((nr, nc))
            stack = new_stack
            dist += 1

        return dist
```

# Oral:
Since we are guaranteed to have two islands, we can begin by traversing the grid until we find an island cell. Starting from the island cell, we apply the DFS algorithm to retrieve all the cells within that island.

After identifying the island, we proceed by starting the cells within that island. Now we employ the BFS algorithm to determine the shortest path from the found island to the other island. We consider cells with value `0` as potential path and continue the search until we encounter an unvisited cell with a value of `1`.

+ Time Complexity: O(n^2)
+ Space Complexity: O(n^2)
