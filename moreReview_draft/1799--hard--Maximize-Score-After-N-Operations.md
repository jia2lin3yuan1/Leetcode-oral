#[1799. Maximize Score After N Operations](https://leetcode.com/problems/maximize-score-after-n-operations/) 
+ `Hard`

You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
```
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.
```
The function gcd(x, y) is the greatest common divisor of x and y.


+ Example 1:

```
Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
```

+ Example 2:

```
Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
```

+ Example 3:

```
Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
```


+ Constraints:

```
1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 106
```

# Solution:
```python {.line-numbers}
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        N = len(nums)

        # compute the gcd over each possible pair of elements in nums
        grid = [[0] * N for _ in range(N)]
        for r in range(N):
            for c in range(r+1, N):
                grid[r][c] = gcd(nums[r], nums[c])

        # dynamic programming solution
        # be careful on the bit optimizations.
        dp = [0] * (1<<N)
        for state in range(1, 1<<N):
            cnt = bin(state).count('1')
            if cnt % 2 != 0:
                continue

            i = cnt // 2
            for r in range(N):
                if state & (1 << r) == 0:
                    continue
                for c in range(r+1, N):
                    if state & (1 << c) == 0:
                        continue
                    pre_state = state ^ (1 << r) ^ (1 << c)
                    dp[state] = max(dp[state], dp[pre_state] + i * grid[r][c])

        return dp[(1<<N) - 1]
```

# Oral:
