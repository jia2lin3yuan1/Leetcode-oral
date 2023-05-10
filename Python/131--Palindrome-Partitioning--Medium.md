# [131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/description/) 
+ `Medium`


Given a string s, partition s such that every
substring
 of the partition is a
palindrome
. Return all possible palindrome partitioning of s.


+ Example 1:

```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
```

+ Example 2:

```
Input: s = "a"
Output: [["a"]]
```


+ Constraints:

```
1 <= s.length <= 16
s contains only lowercase English letters.
```


# Solution:
```python {.line-numbers}
class Solution:
    def is_palindrome(self, st, end, s, palF):
        if st >= end:
            return 1
        if palF[st][end] >= 0:
            return palF[st][end]

        palF[st][end] = self.is_palindrome(st+1, end-1, s, palF) if s[st]==s[end] else 0
        return palF[st][end]


    def partition(self, s: str) -> List[List[str]]:
        palF  = [[-1] * len(s) for _ in range(len(s))]
        dp    = dict() # dp[k]: possible palindrome partitioning of s[:k]
        dp[0] = [[]]

        for k in range(len(s)):
            dp[k+1] = []
            for j in range(k+1):
                if self.is_palindrome(j, k, s, palF):
                    dp[k+1] += [ele + [s[j:k+1]] for ele in dp[j]]
        return dp[len(s)]
```

# Oral:
This is a DP problem. To solve it, we define the DP formation as: (### m)
	
    `dp[k+1] = Union( [ ele + s[j:k+1] for ele in dp[j] if s[j:k+1] is palindrome ])`

Where, dp[k] represents all possible palindrome partitioning of s[:k]

In implementation, we first implement the way to decide if a substring is palindrome.
Then, we call the DP formulation within the for loop that going through s.

The time complexity is: O(N^3).

The spatial complexity is: O(2^N)
