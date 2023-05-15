#[2382. Maximum Segment Sum After Removals](https://leetcode.com/problems/maximum-segment-sum-after-removals/description/)
+ `Hard`

You are given two 0-indexed integer arrays nums and removeQueries, both of length n. For the ith query, the element in nums at the index removeQueries[i] is removed, splitting nums into different segments.

A segment is a contiguous sequence of positive integers in nums. A segment sum is the sum of every element in a segment.

Return an integer array answer, of length n, where answer[i] is the maximum segment sum after applying the ith removal.

Note: The same index will not be removed more than once.


+ Example 1:

```
Input: nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]
Output: [14,7,2,2,0]
Explanation: Using 0 to indicate a removed element, the answer is as follows:
Query 1: Remove the 0th element, nums becomes [0,2,5,6,1] and the maximum segment sum is 14 for segment [2,5,6,1].
Query 2: Remove the 3rd element, nums becomes [0,2,5,0,1] and the maximum segment sum is 7 for segment [2,5].
Query 3: Remove the 2nd element, nums becomes [0,2,0,0,1] and the maximum segment sum is 2 for segment [2]. 
Query 4: Remove the 4th element, nums becomes [0,2,0,0,0] and the maximum segment sum is 2 for segment [2]. 
Query 5: Remove the 1st element, nums becomes [0,0,0,0,0] and the maximum segment sum is 0, since there are no segments.
Finally, we return [14,7,2,2,0].
```

+ Example 2:

```
Input: nums = [3,2,11,1], removeQueries = [3,2,1,0]
Output: [16,5,3,0]
Explanation: Using 0 to indicate a removed element, the answer is as follows:
Query 1: Remove the 3rd element, nums becomes [3,2,11,0] and the maximum segment sum is 16 for segment [3,2,11].
Query 2: Remove the 2nd element, nums becomes [3,2,0,0] and the maximum segment sum is 5 for segment [3,2].
Query 3: Remove the 1st element, nums becomes [3,0,0,0] and the maximum segment sum is 3 for segment [3].
Query 4: Remove the 0th element, nums becomes [0,0,0,0] and the maximum segment sum is 0, since there are no segments.
Finally, we return [16,5,3,0].
```
 

+ Constraints:

```
n == nums.length == removeQueries.length
1 <= n <= 105
1 <= nums[i] <= 109
0 <= removeQueries[i] < n
All the values of removeQueries are unique.
```

# Solution:
```python {.line-numbers}
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:

        N = len(nums)

        # compute the left accumulated sum
        acc_sum = [0] * (N + 1)
        for k, v in enumerate(nums):
            acc_sum[k + 1] = acc_sum[k] + nums[k]

        left, right  = [-1] * N, [-1] * N
        maxSum, ans  = 0, [0]
        for i in range(N-1, 0, -1):
            k = removeQueries[i]
            if not self.hasLeftCombine(k, left) and not self.hasRightCombine(k, right, N):
                left[k], right[k] = k, k
            elif not self.hasLeftCombine(k, left):
                left[k] = k
                if k == N - 1:
                    right[k] = k
                else:
                    left[right[k + 1]] = k
                    right[k] = right[k + 1]

            elif not self.hasRightCombine(k, right, N):
                if k == 0:
                    left[k] = k
                else:
                    left[k] = left[k-1]
                    right[left[k-1]] = k
                right[k] = k
            else:
                left[k], right[k] = left[k-1], right[k + 1]
                left[right[k + 1]] = left[k]
                right[left[k - 1]] = right[k]

            maxSum = max(acc_sum[right[k] + 1] - acc_sum[left[k]], maxSum)
            ans.insert(0, maxSum)

        return ans


    def hasLeftCombine(self, k, left):
        if k == 0:
            return False
        elif left[k-1] == -1:
            return False

        return True

    def hasRightCombine(self, k, right, N):
        if k == N-1:
            return False
        elif right[k + 1] == -1:
            return False

        return True
```

# [zhihu solution introduction](https://zhuanlan.zhihu.com/p/564881037)

# Oral:
