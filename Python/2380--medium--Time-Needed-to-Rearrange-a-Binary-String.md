#[2380. Time Needed to Rearrange a Binary String](https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/description/) 
+ `Medium`

You are given a binary string s. In one second, all occurrences of "01" are simultaneously replaced with "10". This process repeats until no occurrences of "01" exist.

Return the number of seconds needed to complete this process.


+ Example 1:

```
Input: s = "0110101"
Output: 4
Explanation: 
After one second, s becomes "1011010".
After another second, s becomes "1101100".
After the third second, s becomes "1110100".
After the fourth second, s becomes "1111000".
No occurrence of "01" exists any longer, and the process needed 4 seconds to complete,
so we return 4.
```

+ Example 2:

```
Input: s = "11100"
Output: 0
Explanation:
No occurrence of "01" exists in s, and the processes needed 0 seconds to complete,
so we return 0.
```
 

+ Constraints:

```
1 <= s.length <= 1000
s[i] is either '0' or '1'.
```

# Solution:
```python {.line-numbers}
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        N = len(s)
        new_s, k, swap = '', 0, False
        while k < N:
            if k < N-1 and s[k] == '0' and s[k+1] == '1':
                new_s, k, swap = new_s + '10', k + 2, True
            else:
                new_s, k = new_s + s[k], k + 1

        if not swap:
            return 0
        else:
            return 1 + self.secondsToRemoveOccurrences(new_s)


    def secondsToRemoveOccurrences_math(self, s: str) -> int:
        ans = 0
        zeros = 0

        for v in s:
            if v == '0':
                zeros += 1
            elif zeros > 0:
                ans = max(ans + 1, zeros)

        return ans
```

# Oral:
+ Brute force solution
    
    There is a brute force solution that can recursively solve the problem. In each iteration, we traverse the string and update every occurrency of `01` in `s` to `10` in `new_s`. If a swap process occurs, we return `1` plus on the recursive call to the function using the updated input `out_s`. If no swap process occurs, we return `0`. 
    
    - Time Complexity: O(N^2)
    - Space Complexity: O(N^2) 

+ math solution

    Analysis the problem with math, if we traverse the string, regarding an element `v` in `s`, there are two cases:
    - if `v = 1`:
       + if there is no `0` ahead of `v`, no need to do swap process.
       + else (there are zeros ahead of `v`), 
            - there are more `1` ahead of `v`, the number of swap equals to the maximum of the number of swaps in last step plus one 
            - there are more `0` ahead of `v`, the number of swap equals to the number of zeros ahead of `v`.
         In summary, we take the maximum of the two cases in this case.

    - if `v = 0`, we accumulate the occurence of zeros.

    - Time Complexity: O(N)
    - Space Complexity: O(1)
