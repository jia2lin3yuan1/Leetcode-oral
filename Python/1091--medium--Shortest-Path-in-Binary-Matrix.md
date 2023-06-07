#[1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/description/) 
+ `Medium`

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

```
All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
```
The length of a clear path is the number of visited cells of this path.



+ Example 1:
```
Input: grid = [[0,1],[1,0]]
Output: 2
```
+ Example 2:
```
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
```
+ Example 3:
```
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
```

+ Constraints:

```
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
```

# Solution:
```python {.line-numbers}
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        N = len(grid)
        visited = [[False] * N for _ in range(N)]

        # BFS search
        stack, visited[0][0] = [(0, 0, 1)], True
        while(len(stack) > 0):
            r, c, length = stack.pop(0)
            if r == N-1 and c == N-1:
                return length
            for nr in range(r - 1, r + 2):
                for nc in range(c - 1, c + 2):
                    if self.invalidLocation(nr, nc, N):
                        continue
                    if grid[nr][nc] == 0 and not visited[nr][nc]:
                        stack.append((nr, nc, length + 1))
                        visited[nr][nc] = True

        return -1

    def invalidLocation(self, r, c, N):
        if r < 0 or r >= N:
            return True
        elif c < 0 or c >= N:
            return True
        else:
            return False
```



# Oral:
The problem is a traditional shortest path problem in graph, where the graph can be represented as a tree or an array. We use the BFS search algorithm to solve it. In the implementation, we utilize a variable `stack` to store the nodes that need to be processed, and a variable `visited` to mask the visited nodes and avoid revisiting them. The `stack` is initially set to contain the source node with a length `1`. Then we excute a while loop to pop and push nodes until we reach the destination node or the length of `stack` becomes `0`.

Time complexity: O(N^2)
Space complexity: O(N^2)
