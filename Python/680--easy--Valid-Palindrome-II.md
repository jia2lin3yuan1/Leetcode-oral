#[680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/description/) 
+ `Easy`

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

+ Example 1:

```
Input: s = "aba"
Output: true
```

+ Example 2:

```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```

+ Example 3:

```
Input: s = "abc"
Output: false
```


+ Constraints:

```
1 <= s.length <= 105
s consists of lowercase English letters.
```

# Solution:
```python {.line-numbers}
class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.isPalindrome(0, len(s)-1, s, 0)

    def isPalindrome(self, st, end, s, delete=0):
        if st >= end:
            return True
        
        if s[st] != s[end]:
            if delete > 0:
                return False
            else:
                if self.isPalindrome(st+1, end, s, delete+1):
                    return True
                if self.isPalindrome(st, end-1, s, delete + 1):
                    return True
                return False
        else:
            return self.isPalindrome(st+1, end-1, s, delete)
```

# Oral:

This is a DP question and can be solved recursively. Each time we compare the head letter and tail letter and then call the same function to check if the rest of the string is a palindrome under the given requirements.

Here, the recursive function has arguments `st` and `end` to record the location to be checked at current call. It also has a variable `delete` to count how many deletion operations have been peformed.

At each call, we compare `st` and `end`, and `s[st]` and `s[end]` to check if an edge case is reached, and how to move forward if it is not an edge case.

Time complexity: O(N)

Space complexity: O(1)
