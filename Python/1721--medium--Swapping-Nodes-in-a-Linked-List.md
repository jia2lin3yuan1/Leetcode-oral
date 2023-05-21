#[1721. Swapping Nodes in a Linked List](https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/) 
+ `Medium`

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).


+ Example 1:

```
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
```

+ Example 2:

```
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
```

+ Constraints:

```
The number of nodes in the list is n.
1 <= k <= n <= 105
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
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # first travesal to compute the length
        length = 0
        node = head
        while node is not None:
            length += 1
            node = node.next
        
        # check if no need to swap
        if length == 2 * k - 1:
            return head
        
        # swap lft and rht to ensure lft is smaller than length/2
        lft, rht = k, length - k + 1
        if lft > rht:
            lft, rht = rht, lft

        # 2nd travesal to locate the first and second node
        fst, scd = None, None
        node, cnt = head, 1
        while node is not None:
            if cnt == lft:
                fst = node
            elif cnt == rht:
                scd = node
                break
            cnt += 1
            node = node.next

        # swap value
        fst.val, scd.val = scd.val, fst.val

        return head
```

# Oral:
In order to get the `kth` node from the end, we need to first iterate over the list to get the length of the list.

If `k == length - k + 1`, we don't need to swap the nodes. Can return the head directly.

If `k > length/2`, we can swap `k` and `length - k + 1` to ensure the `kth` node from the begining is always on the left. After that, we do second iteration over the list and find the `kth` node from the begining and the `kth` node from the end. At last, swap the values.

Time complexity: O(N)

Space complexity: O(1)
