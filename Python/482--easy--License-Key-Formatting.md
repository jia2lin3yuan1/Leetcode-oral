# 482. License Key Formatting
+ Easy

You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

+ Example 1:
```
Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
```

+ Example 2:

```
Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
```

+ Constraints:

```
1 <= s.length <= 105
s consists of English letters, digits, and dashes '-'.
1 <= k <= 104
```

# Solution:
```Python
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        length = len(s)

        output = ''
        cur_cnt = 0
        for i in range(length-1, -1, -1):
            if s[i] == '-':
                continue
            else:
                if cur_cnt >= k:
                    cur_cnt, output = 0, '-' + output

                cur_cnt += 1
                output = s[i] + output

        return output.upper()
```

# Oral:

To reformat the string under the given rules, we iterative through the input string `s` from end to the begining. We initialize the output_str as an empty string and a count meter as 0. Then iterate s starting from the right side,
```bash
if the charactor is '-', continue
if the charactor is a letter, 
    if added 'k' letters, set the count meter to 0 and add '-' to the output_str 
    
    add the letter to the head of output_str and add 1 to the count meter
```

We check the count meter before add the letter to output_str is to avoid adding '-' to the first group in output_str.

Time complexity: O(N)

Space complexity: O(N)
