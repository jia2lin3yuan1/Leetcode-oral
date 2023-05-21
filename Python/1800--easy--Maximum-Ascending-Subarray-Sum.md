#[1800. Maximum Ascending Subarray Sum](https://leetcode.com/problems/maximum-ascending-subarray-sum/description/) 
+ `Easy`

Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.


+ Example 1:

```
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
```

+ Example 2:

```
Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
```

+ Example 3:

```
Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
```


+ Constraints:

```
1 <= nums.length <= 100
1 <= nums[i] <= 100
```

# Solution:
```python {.line-numbers}
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        cur_sum = 0
        for k in range(len(nums)):
            if k == 0 or nums[k] <= nums[k-1]:
                max_sum = max(max_sum, cur_sum)
                cur_sum = nums[k]
            else:
                cur_sum += nums[k]

        return max(max_sum, cur_sum)
```

# Oral:
To solve this problem, we traverse the list. When we encounter `nums[k] <= nums[k-1]`, it indicates the end of an ascending subarray. At this point, we update the `max_sum` value and reset the accumulated local sum as `nums[k]`. Otherwise, if `nums[k] > nums[k-1]`,  we add the element `nums[k]` to the accumulated local sum.

At last, return the maximum of `max_sum` and the last local sum.

Time complexity: O(N)

Space complexity: O(1)

