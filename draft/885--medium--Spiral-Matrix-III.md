#[885. Spiral Matrix III](https://leetcode.com/problems/spiral-matrix-iii/description/) 
+ `Medium`
+ open the link to view visualization explanation.

You start at the cell `(rStart, cStart)` of an `rows x cols` grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all `rows * cols` spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.


+ Example 1:

```
Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
```

+ Example 2:

```
Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
```


+ Constraints:

```
1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
```

# Solution:
```python {.line-numbers}
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        spiral = [[rStart, cStart]]
        for k in range(1, max(rows, cols)):
            st_r  = rStart - k
            end_c = cStart + k
            self.generateRound(st_r, end_c, k*2 + 1, spiral, rows, cols)
        
        return spiral

    
    def generateRound(self, st_r, end_c, edge_size, spiral, rows, cols):
        end_r = edge_size + st_r - 1
        st_c  = end_c - edge_size + 1

        # right edge
        if end_c < cols:
            for r in range(st_r+1, end_r+1):
                if r >= 0 and r < rows:
                    spiral.append([r, end_c])
                
        # bottome edge
        if end_r < rows:
            for c in range(end_c-1, st_c-1, -1):
                if c >= 0 and c < cols:
                    spiral.append([end_r, c])

        # left edge
        if st_c >= 0:
            for r in range(end_r-1, st_r-1, -1):
                if r >= 0 and r < rows:
                    spiral.append([r, st_c])
        
        # top edge
        if st_r >= 0:
            for c in range(st_c+1, end_c+1):
                if c >= 0 and c < cols:
                    spiral.append([st_r, c])
```

# Oral:
