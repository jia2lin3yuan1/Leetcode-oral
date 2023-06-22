#[2448. Minimum Cost to Make Array Equal](https://leetcode.com/problems/minimum-cost-to-make-array-equal/description/) 
+ `Hard`

You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

```
Increase or decrease any element of the array nums by 1.
```

The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.


+ Example 1:

```
Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.
```

+ Example 2:

```
Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.
```


+ Constraints:

```
n == nums.length == cost.length
1 <= n <= 10^5
1 <= nums[i], cost[i] <= 10^6
```

# Solution:
```python {.line-numbers}
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        N = len(nums)
        sorted_idx = sorted(range(N), key=lambda i: nums[i])
    
        acc_cost = [0] * (N + 1)
        for k, sidx in enumerate(sorted_idx):
            acc_cost[k + 1] = acc_cost[k] + cost[sidx]
        
        # compute the cost for changing all element to element sorted_idx[0].
        sel_idx, cost_sel = sorted_idx[0], 0
        for sidx in sorted_idx[1:]:
            cost_sel += (nums[sidx] - nums[sel_idx]) * cost[sidx]
        
        # compute the cost for changing all element to element with larger value step by step.
        ans = cost_sel
        for k in range(1, N):
            diffV = nums[sorted_idx[k]] - nums[sorted_idx[k - 1]]

            # 0 ~ k - 1, increase cost
            lft_inc = (acc_cost[k] - acc_cost[0]) * diffV

            # k ~ N-1, decrease cost 
            rht_dec = (acc_cost[N] - acc_cost[k]) * diffV

            cost_sel = cost_sel + lft_inc - rht_dec
            ans = min(ans, cost_sel)
            
        
        return ans
```

# Oral:
Assume `nums` is in ascending order and refered to as `nums_inc`, and the corresponding `cost` is denoted as `cost*`, the cost of changing all elements to `nums_inc[k]` is computed with two steps:
```
1. calculate the difference between nums_inc[k] and nums_inc[k-1], and store it as diffV.
        diffV = nums_inc[k] - nums_inc[k - 1]

2. compute the total cost using the equation:
        change[k] = change[k-1] + sum(cost*[0, ..., k-1]) * diffV - sum(cost*[k, ..., N-1]) * diffV 
```
Here, sum of `cost*` can be computed efficiently in constant time using accumulated sums.

Therefore, to implement this algorithm, we begin by performing an argsort on `nums` and computing the accumulated sum of `cost*`. Then, we compute the total cost of changing all elements in nums to `nums_inc[0]` with a for-loop. At last, we iterate over `1` to `N-1` to compute their total cost with the equation and maintain the minimum total cost.

Time complexity: O(NlogN)

space complexity: O(N)
