#[2381. Shifting Letters II](https://leetcode.com/problems/shifting-letters-ii/description/) 
+ `Medium`

You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.



+ Example 1:

```
Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
```

+ Example 2:

```
Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
```


+ Constraints:

```
1 <= s.length, shifts.length <= 5 * 104
shifts[i].length == 3
0 <= starti <= endi < s.length
0 <= directioni <= 1
s consists of lowercase English letters.
```

# Solution:
```python {.line-numbers}
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        letter2idx_lut = {e: k for k, e in enumerate(letters)}

        shift_stats = [0] * len(s)
        for ele in shifts:
            shift_stats[ele[0]] += 1 if ele[2] == 1 else -1
            if ele[1] + 1 < len(s):
                shift_stats[ele[1] + 1] += -1 if ele[2] == 1 else 1

        s_list = list(s)
        change = 0
        for k, (letter, s) in enumerate(zip(s_list, shift_stats)):
            change += s
            s_list[k] = letters[(letter2idx_lut[letter] + change) % 26]
        return ''.join(s_list)


    def shiftingLetters_bruteforce_outTime(self, s: str, shifts: List[List[int]]) -> str:
        
        letters = 'abcdefghijklmnopqrstuvwxyz'
        shift_lut = {e: {'1':letters[(k+1)%26], '0':letters[( k - 1 + 26) % 26]} for k, e in enumerate(letters)}

        s_list = list(s)
        for ele in shifts:
            for k in range(ele[0], ele[1] + 1):
                s_list[k] = shift_lut[s_list[k]][str(ele[2])]
        
        return ''.join(s_list)
```

# Oral:
