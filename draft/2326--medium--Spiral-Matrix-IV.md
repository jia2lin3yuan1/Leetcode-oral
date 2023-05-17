#[2326. Spiral Matrix IV](https://leetcode.com/problems/spiral-matrix-iv/description/) 
+ `Medium`
+ open the link to view visualization explanation.

You are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.


+ Example 1:

```
Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
```

+ Example 2:

```
Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.
```

+ Constraints:

```
1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
```

# Solution:
```python {.line-numbers}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]

        iter_tot = (min(m, n) + 1) // 2 + 1
        node = head
        for k in range(iter_tot):
            if node is not None:
                rsize, csize = m - k * 2, n - k * 2
                node = self.generateRound(k, rsize, csize, node, matrix)
        return matrix
    
    def generateRound(self, k, rsize, csize, node, matrix):
        rend, cend = k + rsize - 1, k + csize - 1
        if rsize == 1:
            for j in range(k, cend + 1):
                matrix[k][j], node = node.val, node.next
                if node is None:
                    return node
        elif csize == 1:
            for j in range(k, rend + 1):
                matrix[j][k], node = node.val, node.next
                if node is None:
                    return node
        else:
            # top edge
            for j in range(k, cend):
                matrix[k][j], node = node.val, node.next
                if node is None:
                    return node
            
            # right edge
            for j in range(k, rend):
                matrix[j][cend], node = node.val, node.next
                if node is None:
                    return node
            
            # bottom edge
            for j in range(cend, k, -1):
                matrix[rend][j], node = node.val, node.next
                if node is None:
                    return node
            
            # left edge
            for j in range(rend, k, -1):
                matrix[j][k], node = node.val, node.next
                if node is None:
                    return node

        return node
```

# Oral:
