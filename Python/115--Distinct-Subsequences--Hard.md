# 115. Distinct Subsequences
+ Hard

Given two strings s and t, return the number of distinct
subsequences
 of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

+ Example 1:
```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
```

+ Example 2:

```
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
```


+ Constraints:
```
1 <= s.length, t.length <= 1000
s and t consist of English letters.
```

# Solution:
```Python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # create lut for target
        target_lut = dict()
        for k, v in enumerate(t):
            if v not in target_lut:
                target_lut[v] = []
            # insert at head, so that the update order in line 17~18 is correct
            target_lut[v].insert(0, k)


        # go through string
        dp = [0] * (len(t) + 1) # dp[k+1]: number of appearance of t[:k]
        dp[0] = 1
        for v in s:
            if v not in target_lut:
                continue
            for tk in target_lut[v]:
                dp[tk+1] += dp[tk]

        return dp[-1]
```

# Oral:
We can use DP to solve this problem. First, we create a list to record the DP status, where : (### its kth element means the number of the subsequence: the first k values in t)
        ``` dp[k]: number of subsequence t[:k-1] 
        ```

The list dp is at length (len(t) + 1), it is initialized as dp[0] = 1 and all 0 in other locations.

When we go through each character v in s, if it equals to a character tc in t at tk,( tc == v), run the DP formulation, that : (### dp[tk+1] equals to adding the dp[tk] to dp[tk+1] )
       ``` dp[tk + 1] += dp[tk] 
       ```

To accelerate the speed, we create a LUT for t, where: ( ### the keys are unique characters appeared in t, and the value is a list of the location where the key is in t )
       ```target_lut = {tc: [tk_0, tk_1], …}
       ```

Finally, dp[-1] is the answer

```
The time complexity is: O(L_s * L_k).
The spatial complexity is: O(max(L_s, L_k))
```
