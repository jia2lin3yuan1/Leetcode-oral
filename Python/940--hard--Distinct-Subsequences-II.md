# [940. Distinct Subsequences II](https://leetcode.com/problems/distinct-subsequences-ii/description/) 
+ `Hard`
Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.
 

+ Example 1:

```
Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
```

+ Example 2:

```
Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".
```

+ Example 3:

```
Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
```
 

+ Constraints:

```
1 <= s.length <= 2000
s consists of lowercase English letters.
```


# Solution:
```python {.line-numbers}
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        '''
        There are 26 different subsequences, those ending with each letter.
        Iterative over s, on new letter, i.e. 'v':
            -- the subsequences ending with non 'v', their number are not changed.
            -- the new subsequences ending with 'v', including 3 cases:
            ** subsequences ending with non 'v' add the new letter, has at least 2 letter and 1 'v' at the end.
            ** subsequences ending with 'v' add the new letter, has at least 2 'v' at the end.
            ** the subsequence 'v' itself.
        '''
        a2z_s = string.ascii_lowercase
        end_lut = {c: 0 for c in a2z_s}

        mod = int(1e9 + 7)
        for v in s:
            end_lut[v] = (sum([end_lut[c] for c in end_lut]) + 1) % mod

        tot = sum([end_lut[c] for c in end_lut]) % mod
        return tot
```

# Oral:
There are 26 different subsequences, those ending with each letter. We can create a dictionary to record the number of the 26 different subsequences. Then we use dynamic programming to solve this problem.

Iterative over s, on new letter, i.e. 'v':
```
    -- the subsequences ending with non 'v', their number are not changed.
    -- the new subsequences ending with 'v', including 3 cases:
        ** subsequences ending with non 'v' add the new letter, has at least 2 letter and 1 'v' at the end.
        ** subsequences ending with 'v' add the new letter, has at least 2 'v' at the end.
        ** the subsequence 'v' itself.
```
  So, only need to update the dictionary with key 'v': end_lut['v'] = sum(end_lut) + 1

Finally, the sum of the whole dictionary is the number of distinct subsequences.

The time complexity is: O(N).

The spatial complexity is: O(1)
