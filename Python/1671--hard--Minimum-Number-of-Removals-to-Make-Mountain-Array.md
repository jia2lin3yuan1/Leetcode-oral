#[1671. Minimum Number of Removals to Make Mountain Array](https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/) 
+ `Hard`

You may recall that an array arr is a mountain array if and only if:

```
arr.length >= 3
```

There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
```
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
```
Given an integer array nums, return the minimum number of elements to remove to make nums a mountain array.



+ Example 1:

```
Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.
```

+ Example 2:

```
Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
```


+ Constraints:

```
3 <= nums.length <= 1000
1 <= nums[i] <= 109
It is guaranteed that you can make a mountain array out of nums.
```

# Solution:
```python {.line-numbers}
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        '''
        Solve this problem with LIS / LDS
        from left to right, compute the longest increasing length ends with each element in nums,
        from right to left, compute the longest decreasing length ends with each element in nums

        Thus, the candidate mountain peak is the element with increasing length > 0 and decreasing length > 0

        To compute the longest increasing length, using 2 for-loops.
        '''
        inc_cnt = self.countStatus(nums, order=0)
        dec_cnt = self.countStatus(nums, order=1)

        num_del = min([len(nums) - ic - dc - 1 for ic, dc in zip(inc_cnt,dec_cnt) \
                                                if ic > 0 and dc > 0])
        return num_del


    def countStatus(self, nums, order = 0):
        order_cnt = [0] * len(nums)
        check_order = [k for k in range(len(nums))] if order == 0 else \
                        [len(nums) - 1 - k for k in range(len(nums))]

        preV      = nums[check_order[0]]
        for k in range(1, len(nums)):
            cur = check_order[k]
            for j in range(k):
                pre = check_order[j]
                if nums[cur] <= nums[pre]:
                    continue
                order_cnt[cur] = max(order_cnt[cur], order_cnt[pre] + 1)

        return order_cnt
```

# Oral:
Solve this problem with LIS / LDS

```
from left to right, compute the longest increasing length ends with each element in nums,
from right to left, compute the longest decreasing length ends with each element in nums
```

Thus, the candidate mountain peak is the element with increasing length > 0 and decreasing length > 0

To compute the longest increasing length, using 2 for-loops.

The time complexity is: O(N^2).

The spatial complexity is: O(N)
