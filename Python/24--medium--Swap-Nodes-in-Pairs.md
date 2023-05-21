#[24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/description/) 
+ `Medium`
+ open the link to view visualization explanation

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


+ Example 1:

```
Input: head = [1,2,3,4]
Output: [2,1,4,3]
```

+ Example 2:

```
Input: head = []
Output: []
```


+ Example 3:

```
Input: head = [1]
Output: [1]
```


+ Constraints:

```
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
```

# Solution:
```python {.line-numbers}
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a node point to head, so that each node has its pre-node
        new_head = ListNode(next = head)

        # moving forward with 2 nodes at each step
        pNode, node = new_head, head
        while node is not None and node.next is not None:
            nNode = node.next
            pNode.next, nNode.next, node.next = nNode, node, nNode.next
            pNode, node = node, node.next

        return new_head.next
```

# Oral:
When dealing with linked list questions, it is important to pay attention to the pointers.

To swap each pair of adjacent nodes`(node, n_Node)` in this problem, let's assume the node point to `node` is `p_Node`, the relevant pointers involved in the swap include: `p_Node.next, node.next`, and `n_Node.next`. We need to update these three pointers so that the new order becomes `p_Node, n_Node, node`.

After completing the swapping process, we assign `node, node.next` as the new `p_Node, node`, respectively. It will allow us to move forward and swap the next two adjacent nodes if they exist.

Time complexity: O(N)

Space complexity: O(1)
