#[1630. Arithmetic Subarrays](https://leetcode.com/problems/arithmetic-subarrays/description/) 
+ `Medium`

A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.


+ Example 1:

```
Input: nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
Output: [true,false,true]
Explanation:
In the 0th query, the subarray is [4,6,5]. This can be rearranged as [6,5,4], which is an arithmetic sequence.
In the 1st query, the subarray is [4,6,5,9]. This cannot be rearranged as an arithmetic sequence.
In the 2nd query, the subarray is [5,9,3,7]. This can be rearranged as [3,5,7,9], which is an arithmetic sequence.
```

+ Example 2:

```
Input: nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
Output: [false,true,false,false,true,true]
```


+ Constraints:

```
n == nums.length
m == l.length
m == r.length
2 <= n <= 500
1 <= m <= 500
0 <= l[i] < r[i] < n
-105 <= nums[i] <= 105
```

# Solution:
```python {.line-numbers}
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # sort in increasing order and return the sorted_idx
        sort_idx = sorted(range(len(nums)), key=lambda i: nums[i])

        ans = []
        # for eqch query, iterate over the array in sorted_idx order.
        for lq, rq in zip(l, r):
            flag, preV, base = 0, None, None
            for sk in sort_idx:
                if sk < lq or sk > rq:
                    continue

                if base is not None and nums[sk] - preV != base:
                    ans.append(False)
                    break
                elif preV is not None and base is None:
                    base = nums[sk] - preV

                preV = nums[sk]
                flag += 1
                if flag == (rq - lq + 1):
                    ans.append(True)
                    break
        return ans
```

# Oral:
For the arithmitic array problem, where it requires the re-arraged array needs to increase with an equal step, it becomes straightforward to determine if the array has been sorted in increasing order.

To efficiently handle multiple queries involving index ranges, we sort the array and return the sorted indices. This allows us to check each query in O(N) time complexity. In detail, we iterate over the sorted indices, and when we meet an element within the the query range, we compute the step `base` when we meet two valid elements and keep track of the previous element. By comparing the difference between each value and its previous value with `base`, we can determine if it satisfies the requirement for an arithmetic array.

- time complexity: O(max(NlogN, MN))
- space complexity:O(M) 
