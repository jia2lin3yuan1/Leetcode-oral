#[713. Subarray Product Less Than K](https://leetcode.com/problems/subarray-product-less-than-k/description/) 
+ `Medium`

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.


+ Example 1:
```
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
```

+ Example 2:

```
Input: nums = [1,2,3], k = 0
Output: 0
```


+ Constraints:

```
1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
```

# Solution:
```python {.line-numbers}
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        acc_product, ans = 1, 0

        # two pointers to iterate over the array. 
        # When acc_product >= k, move the lft pointer.
        lft, rht  = 0, 0
        while rht < N:
            acc_product *= nums[rht]
            while acc_product >= k and lft <= rht:
                acc_product /= nums[lft]
                lft += 1
            
            ans, rht = ans + rht - lft + 1, rht + 1
        
        return ans
```

# Oral:
