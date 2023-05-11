#[501. Find Mode in Binary Search Tree](https://leetcode.com/problems/find-mode-in-binary-search-tree/description/) 
+ `Easy`

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


+ Example 1:

```
Input: root = [1,null,2,2]
Output: [2]
```

+ Example 2:

```
Input: root = [0]
Output: [0]
```


+ Constraints:

```
The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
```

# Solution:
```python {.line-numbers}
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        mode_lut = dict()

        while len(stack) > 0:
            top = stack.pop(0)
            if top is None:
                continue
                
            if top.val not in mode_lut:
                mode_lut[top.val] = 1
            else:
                mode_lut[top.val] += 1

            stack.append(top.left)
            stack.append(top.right)
        
        print(mode_lut)
        max_cnt = max([ele[1] for ele in mode_lut.items()])
        modes = [ele[0] for ele in mode_lut.items() if ele[1] == max_cnt]

        return modes
```

# Oral:
