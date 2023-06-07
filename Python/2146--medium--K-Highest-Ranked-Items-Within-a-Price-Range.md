#[2146. K Highest Ranked Items Within a Price Range](https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/description/) 
+ `Medium`

+ open the link for visualize example

You are given a 0-indexed 2D integer array grid of size m x n that represents a map of the items in a shop. The integers in the grid represent the following:

```
0 represents a wall that you cannot pass through.
1 represents an empty cell that you can freely move to and from.
All other positive integers represent the price of an item in that cell. You may also freely move to and from these item cells.
It takes 1 step to travel between adjacent grid cells.
```

You are also given integer arrays pricing and start where pricing = [low, high] and start = [row, col] indicates that you start at the position (row, col) and are interested only in items with a price in the range of [low, high] (inclusive). You are further given an integer k.

You are interested in the positions of the k highest-ranked items whose prices are within the given price range. The rank is determined by the first of these criteria that is different:

Distance, defined as the length of the shortest path from the start (shorter distance has a higher rank).
Price (lower price has a higher rank, but it must be in the price range).
The row number (smaller row number has a higher rank).
The column number (smaller column number has a higher rank).
Return the k highest-ranked items within the price range sorted by their rank (highest to lowest). If there are fewer than k reachable items within the price range, return all of them.


+ Example 1:

```
Input: grid = [[1,2,0,1],[1,3,0,1],[0,2,5,1]], pricing = [2,5], start = [0,0], k = 3
Output: [[0,1],[1,1],[2,1]]
Explanation: You start at (0,0).
With a price range of [2,5], we can take items from (0,1), (1,1), (2,1) and (2,2).
The ranks of these items are:
- (0,1) with distance 1
- (1,1) with distance 2
- (2,1) with distance 3
- (2,2) with distance 4
Thus, the 3 highest ranked items in the price range are (0,1), (1,1), and (2,1).
```

+ Example 2:


```
Input: grid = [[1,2,0,1],[1,3,3,1],[0,2,5,1]], pricing = [2,3], start = [2,3], k = 2
Output: [[2,1],[1,2]]
Explanation: You start at (2,3).
With a price range of [2,3], we can take items from (0,1), (1,1), (1,2) and (2,1).
The ranks of these items are:
- (2,1) with distance 2, price 2
- (1,2) with distance 2, price 3
- (1,1) with distance 3
- (0,1) with distance 4
Thus, the 2 highest ranked items in the price range are (2,1) and (1,2).
```


+ Example 3:


```
Input: grid = [[1,1,1],[0,0,1],[2,3,4]], pricing = [2,3], start = [0,0], k = 3
Output: [[2,1],[2,0]]
Explanation: You start at (0,0).
With a price range of [2,3], we can take items from (2,0) and (2,1).
The ranks of these items are:
- (2,1) with distance 5
- (2,0) with distance 6
Thus, the 2 highest ranked items in the price range are (2,1) and (2,0).
Note that k = 3 but there are only 2 reachable items within the price range.
```


+ Constraints:

```
m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
0 <= grid[i][j] <= 105
pricing.length == 2
2 <= low <= high <= 105
start.length == 2
0 <= row <= m - 1
0 <= col <= n - 1
grid[row][col] > 0
1 <= k <= m * n
```

# Solution:
```python {.line-numbers}
class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        neighbours = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        M, N     = len(grid), len(grid[0])
        validRow = lambda a : a >= 0 and a < M
        validCol = lambda a: a >= 0 and a < N

        # BFS search
        max_heap, heap_dist = [], k + 1
        visited = [[0] * N for _ in range(M)]
        visited[start[0]][start[1]] = True
        nodes   = [(0, grid[start[0]][start[1]], start[0], start[1])]
        while len(nodes):
            dist, price, r, c = nodes.pop(0)

            # the current node is a valid node
            if price >= pricing[0] and price <= pricing[1]:
                if len(max_heap) == k:
                    if dist > heap_dist: # impossible to get node with higher rank
                        break
                    heapq.heappush(max_heap, (-dist, -price, -r, -c))
                    heapq.heappop(max_heap)
                else:
                    heapq.heappush(max_heap, (-dist, -price, -r, -c))
                heap_dist = dist
            
            # find next level nodes:
            for dr, dc in neighbours:
                nr, nc = r + dr, c + dc
                nc = c + dc
                if not validRow(nr) or not validCol(nc):
                    continue
                if visited[nr][nc] or grid[nr][nc] == 0:
                    continue
                
                nodes.append((dist + 1, grid[nr][nc], nr, nc))
                visited[nr][nc] = True
            
        # construct answer from max_heap
        ans = []
        while(len(max_heap) > 0):
            _, _, topH_r, topH_c = heapq.heappop(max_heap)
            ans.insert(0, [-topH_r, -topH_c])
        return ans
```

# Oral:
To solve a problem of returning k highest-ranked items, we utilize max heap / min heap to store the found items. The ranking is determined by distance, price, row number, and then column number, where distance has the highest priority. Hence, we employ a BFS search algorithm to traverse the grid, while also maintain a max heap to keep track  of the k highest ranked items.

Time complexity: O(N * M)

space complexity: O(N * M)
