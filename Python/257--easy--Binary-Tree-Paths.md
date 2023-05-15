#[257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/description/) 
+ `Easy`

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.


+ Example 1:

```
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

+ Example 2:

```
Input: root = [1]
Output: ["1"]
```

+ Constraints:

```
The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []

        ans, path = [], ""

        self.leafPaths(root, path, ans)
        ans = [ele[2:] for ele in ans]

        return ans
    
    def leafPaths(self, node, prePath, ans):
        '''
        # scalar, string objects, if changed inside the function, it won't affect the outside one.
        # list, dict, customized classobjects, if changed inside the function, the outside variables will change accordingly.
        '''
        prePath += "->" + str(node.val)

        if node.left is None and node.right is None:
            ans.append(prePath)
        else:
            if node.left is not None:
                self.leafPaths(node.left, prePath, ans)
            if node.right is not None:
                self.leafPaths(node.right, prePath, ans)
```

# Oral:

To visit all the leafs, we can do BFS or DFS to traverse the tree and implement it with a recursive function. To print out the path to each leaf, we can pass an argument to remember the path from the root to the visited node.

At a node, if it doesn't have any child, it is a leaf node. We add its path into `ans`.


Given N is the number of leaf nodes in the tree:

Time complexity: O(N)

Space complexity: O(N)
