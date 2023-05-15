#[144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/) 
+ `Easy`

Given the root of a binary tree, return the preorder traversal of its nodes' values.

+ Example 1:

```
Input: root = [1,null,2,3]
Output: [1,2,3]
```

+ Example 2:

```
Input: root = []
Output: []
```

+ Example 3:

```
Input: root = [1]
Output: [1]
```


+ Constraints:
```
The number of nodes in the tree is in the range [0, 100].
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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        '''
        # preOrder: root, left, right
        # inOrder: left, root, right
        # postOrder: left, right, root
        '''
        if root is None:
            return []

        ans, stack = [], [root]
        while len(stack) > 0:
            top = stack.pop()
            ans.append(top.val)

            if top.right is not None:
                stack.append(top.right)
            if top.left is not None:
                stack.append(top.left)
        return ans


    def preorderTraversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        return self.preorderRecursive(root, ans)

    def preorderRecursive(self, root, ans):
        if root is None:
            return ans
        ans.append(root.val)
        self.preorderRecursive(root.left, ans)
        return self.preorderRecursive(root.right, ans)
```

# Oral:
The first step is to make clear what is preorder travesal. It is to do [root, left, right] order visiting through the tree. We can implement it in the recursive version or the iterative version.

+ The recursive travesal: Given a node, if it is not None, print its value to `ans`. Then traverse over its left child first, then its right child.
+ The iterative version: We utilize a stack to hold the nodes to be processed. At each node, we first print its value to `ans`, and then push its right child onto the stack followed by its left child. This ensured that its left child is processed before its right child. 

Time complexity: O(N)

Space complexity: O(N)
