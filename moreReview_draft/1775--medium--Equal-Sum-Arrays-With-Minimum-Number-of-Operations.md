#[1775. Equal Sum Arrays With Minimum Number of Operations](https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/description/) 
+ `Medium`

You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are between 1 and 6, inclusive.

In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.

Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.



+ Example 1:

```
Input: nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums2[0] to 6. nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2].
- Change nums1[5] to 1. nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2].
- Change nums1[2] to 2. nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2].
```

+ Example 2:

```
Input: nums1 = [1,1,1,1,1,1,1], nums2 = [6]
Output: -1
Explanation: There is no way to decrease the sum of nums1 or to increase the sum of nums2 to make them equal.
```

+ Example 3:

```
Input: nums1 = [6,6], nums2 = [1]
Output: 3
Explanation: You can make the sums of nums1 and nums2 equal with 3 operations. All indices are 0-indexed.
- Change nums1[0] to 2. nums1 = [2,6], nums2 = [1].
- Change nums1[1] to 2. nums1 = [2,2], nums2 = [1].
- Change nums2[0] to 4. nums1 = [2,2], nums2 = [4].
```


+ Constraints:

```
1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[i] <= 6
```

# Analysis:

# Solution:
```python {.line-numbers}
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # impossible case
        N1, N2 = len(nums1), len(nums2)
        if N1 > 6 * N2 or N1 * 6 < N2:
            return -1
        
        # construct lookup table for time efficiency.
        lut_1 = {v: 0 for v in range(1, 7)}
        for v in nums1:
            lut_1[v] += 1
        lut_2 = {v: 0 for v in range(1, 7)}
        for v in nums2:
            lut_2[v] += 1

        # swap nums1 and nums2 if needed, so that we only increase nums1 and decrease nums2 to find the target sum.
        sumV_1, sumV_2 = sum(nums1), sum(nums2)
        if sumV_1 > sumV_2:
            sumV_1, sumV_2 = sumV_2, sumV_1
            lut_1, lut_2 = lut_2, lut_1
            N1, N2 = N2, N1
        diff = sumV_2 - sumV_1

        # greedy algorithm, start with replacing element has largest gap.
        ans, gap = 0, 6
        while diff > 0 and gap > 1:
            gap = gap - 1
            cnt = diff // gap

            # starting from longer array
            if N1 > N2:
                cnt_1 = min(cnt, lut_1[6 - gap])
                cnt_2 = min(cnt - cnt_1, lut_2[1 + gap])
            else:
                cnt_2 = min(cnt, lut_2[1 + gap])
                cnt_1 = min(cnt - cnt_2, lut_1[6 - gap])
            
            # the residual '6-gap' in lut_1 and '1+gap' in lut_2 can also do 'gap-1'
            if cnt_1 < lut_1[6 - gap] and gap > 0:
                lut_1[6 - gap + 1] += lut_1[6 - gap] - cnt_1
            if cnt_2 < lut_2[1 + gap] and gap > 0:
                lut_2[1 + gap - 1] += lut_2[1 + gap] - cnt_2

            diff -= (cnt_1 + cnt_2) * gap

            ans += cnt_1 + cnt_2
            # print(f'{diff} - {gap}:: {cnt_1 + cnt_2}')
        return ans

```

# Oral:
