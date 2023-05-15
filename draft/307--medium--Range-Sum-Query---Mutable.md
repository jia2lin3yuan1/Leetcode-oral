#[307. Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/description/) 
+ `Medium`

Given an integer array nums, handle multiple queries of the following types:

```
Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
```

Implement the NumArray class:

- NumArray(int[] nums) Initializes the object with the integer array nums.
- void update(int index, int val) Updates the value of nums[index] to be val.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


+ Example 1:

```
Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
```


+ Constraints:

```
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.
```

# Solution:
```python {.line-numbers}
class SegmentNode:
    def __init__(self, st=0, end=0, val=0, left=None, right=None):
        self.st, self.end, self.val = st, end, val
        self.left, self.right  = left, right

class SegmentTree:
    def __init__(self, nums):
        self.root = self.buildTree(0, len(nums)-1, nums)
    
    def buildTree(self, st, end, nums):
        # Time complexity: O(N^2)
        if st > end:
            return None
        elif st == end:
            return SegmentNode(st, end, nums[st])
        else:
            mid = (st + end) // 2
            left = self.buildTree(st, mid, nums)
            right = self.buildTree(mid+1, end, nums)
            return SegmentNode(st, end, left.val + right.val, left, right)

    def updateLeave(self, index, new_val, old_val):
        # Time complexity: O(logN)
        head = self.root
        while head is not None:
            head.val += new_val - old_val
            mid = (head.st + head.end) // 2
            head = head.left if index <= mid else head.right
    
    def getRangeSum(self, node, st, end):
        # Time complexity: O(logN)
        if node is None or node.end < st or node.st > end:
            return 0
        
        if node.st >= st and node.end <= end:
            return node.val
        else:
            return self.getRangeSum(node.left, st, end) + self.getRangeSum(node.right, st, end)
    

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.segment_tree = SegmentTree(nums)
        

    def update(self, index: int, val: int) -> None:
        self.segment_tree.updateLeave(index, val, self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.segment_tree.getRangeSum(self.segment_tree.root, left, right)

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
```

# Oral:

