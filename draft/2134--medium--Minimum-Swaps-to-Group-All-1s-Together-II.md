#[2134. Minimum Swaps to Group All 1's Together II](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/)
+ `Medium`

A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.

 
+ Example 1:

```
Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.
```

+ Example 2:

```
Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.
```

+ Example 3:

```
Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.
```
 

+ Constraints:

```
1 <= nums.length <= 105
nums[i] is either 0 or 1.
```

# Solution:
```python {.line-numbers}
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        length = len(nums)
        tot_1  = sum(nums)

        sumK = [nums[0]] * length
        for k in range(1, length):
            if k < tot_1:
                sumK[k] = nums[k] + sumK[k - 1]
            else:
                sumK[k] = nums[k] + sumK[k - 1] - nums[k - tot_1]

        for k in range(tot_1-1):
            pk, rk = (k - 1 + length) % length, (k - tot_1 + length) % length
            sumK[k] = nums[k] + sumK[pk] - nums[rk]

        return tot_1 - max(sumK)


    def minSwaps_dp_outTime(self, nums: List[int]) -> int:
        length = len(nums)
        tot_1  = sum(nums)

        cur_idxes = [k for k in range(length)]
        pre_idxes = [k - 1 for k in range(length)]
        pre_idxes[0] = len(nums) - 1

        dp = [0] * length
        for k in range(tot_1):
            new_dp = [nums[ck] + dp[pk] for ck, pk in zip(cur_idxes, pre_idxes)]
            dp = new_dp
        
        return tot_1 - max(dp)
```

# Oral:

+ brute force (dp)

    O(N^2)

+ sliding window
    O(N)
