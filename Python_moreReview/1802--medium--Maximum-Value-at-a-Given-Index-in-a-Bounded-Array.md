#[1802. Maximum Value at a Given Index in a Bounded Array](https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/description/) 
+ `Medium`

You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

```
nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
```
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.



+ Example 1:

```
Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
```

+ Example 2:

```
Input: n = 6, index = 1,  maxSum = 10
Output: 3
```


Constraints:

```
1 <= n <= maxSum <= 109
0 <= index < n
```

# Solution:
```python {.line-numbers}
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            # compute mid by ceil(), so that it will not ended in dead-loop. 
            mid = (left + right + 1) // 2
            if self.sumFunc(mid-1, index) + self.sumFunc(mid, n - index) > maxSum:
                right = mid - 1
            else:
                left = mid

        return left

    def sumFunc(self, a, cnt):
        '''
        # compute sum over arithmetic progression (等差数列)
        # If cnt < a, a0 = a - cnt + 1, an = a, sum = (a0 + an) * cnt /2
        # if cnt >= a, sum = sum([a, a-1, ..., 1])_{len = a} + sum([1, ..., 1]_{len=a - cnt})
        #                  = (a * a(+1) / 2 ) + (a - cnt)
        '''
        if cnt < a:
            return (a + a - cnt + 1) * cnt / 2
        else:
            return (a * (a + 1)) / 2 + (cnt - a)
```

# Oral:
To maximize the value of `nums[index]`, we need to ensure its neighbor elements have decreasing value by `1` as their distance from 'index' increases, until the value reachs `1`. And, we can divide `nums` into two parts:
 + the left part: `[1, ..., 1, 2, ..., nums[index] - 2, nums[index] - 1]`, with length `index`
 + the right part: `[nums[index], nums[index]-1, ..., 2, 1, 1, ..., 1]`, with length `n - index`.

It is apparent that we can utilize the sum function of an arithmetic progression to easily compute the sum of the two parts.

From the definition of the question, the minimum value and maximum value of `nums[index]` is `1` and `maxSum`. Then we can employ the binary search algorithm to find the value ensure the sum of `nums` does not exceed `maxSum`.

Time complexity: O(log maxSum)

Space complexity: O(1)
