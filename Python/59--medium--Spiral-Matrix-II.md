#[59. Spiral Matrix II](https://leetcode.com/problems/spiral-matrix-ii/description/) 
+ `Medium`

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

```
[ 1 -> 2 -> 3 ]
[           | ]
[ 8 -> 9 -> 4 ]
[ |         | ]
[ 7 <- 6 <- 5 ]

```
+ Example 1:

```
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
```

+ Example 2:

```
Input: n = 1
Output: [[1]]
```


+ Constraints:

```
1 <= n <= 20
```

# Solution:
```python {.line-numbers}
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        val_0 = 1
        for k in range((n+1) // 2 + 1):
            edge_size = n - k * 2
            val_0 = self.generateRound(k, val_0, edge_size, matrix)

        return matrix

    def generateRound(self, k, val_0, edge_size, matrix):
        st_k, end_k = k, k + edge_size - 1
        
        if st_k == end_k: # if only one cell
            matrix[st_k][end_k], val_0 = val_0, val_0 + 1
        else:
            # top edge
            for c in range(st_k, end_k):
                matrix[st_k][c], val_0 = val_0, val_0 + 1

            # right edge
            for r in range(st_k, end_k):
                matrix[r][end_k], val_0 = val_0, val_0 + 1

            # bottom edge
            for c in range(end_k, st_k, -1):
                matrix[end_k][c], val_0 = val_0, val_0 + 1

            # left edge
            for r in range(end_k, st_k, -1):
                matrix[r][st_k], val_0 = val_0, val_0 + 1

        return val_0 
```

# Oral:

To simplify the problem, assign a value to each round circle in the matrix. Consequently, we can iterate over `k` from `0` to `(n+1)//2` and assign values to each round.

When assigning a value to one round, consider it as having four edges if the `edge size > 1`. Set a variable $val_0$ that accumulates by `1` to record the value to be assigned in the matrix.

Time complexity: O(n^2)

Space complexity: O(n^2)
