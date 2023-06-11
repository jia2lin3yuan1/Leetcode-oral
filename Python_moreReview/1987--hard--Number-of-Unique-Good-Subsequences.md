#[1987. Number of Unique Good Subsequences](https://leetcode.com/problems/number-of-unique-good-subsequences/) 
+ `Hard`

You are given a binary string binary. A subsequence of binary is considered good if it is not empty and has no leading zeros (with the exception of "0").

Find the number of unique good subsequences of binary.

For example, if binary = "001", then all the good subsequences are ["0", "0", "1"], so the unique good subsequences are "0" and "1". Note that subsequences "00", "01", and "001" are not good because they have leading zeros.
Return the number of unique good subsequences of binary. Since the answer may be very large, return it modulo 109 + 7.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.



+ Example 1:

```
Input: binary = "001"
Output: 2
Explanation: The good subsequences of binary are ["0", "0", "1"].
The unique good subsequences are "0" and "1".
```

+ Example 2:

```
Input: binary = "11"
Output: 2
Explanation: The good subsequences of binary are ["1", "1", "11"].
The unique good subsequences are "1" and "11".
```


+ Example 3:

```
Input: binary = "101"
Output: 5
Explanation: The good subsequences of binary are ["1", "0", "1", "10", "11", "101"].
The unique good subsequences are "0", "1", "10", "11", and "101".
```


+ Constraints:

```
1 <= binary.length <= 105
binary consists of only '0's and '1's.
```

# Solution:
```python {.line-numbers}
class Solution:
        '''
        there are three different type subsequences:
            -- '0'
            -- starting with '1', end-with-zero
            -- starting with '1', end-with-one

        Iterative over the binary string, if the new charactor is '0':
            -- it is sure there will be the subsequence '0'
            -- subsequences end-with-one: number is the same as before.
            -- subsequences end-with-zero has 2 cases:
                ** add the '0' to all subsequences end-with-one, the new subsequences will have 1 zero at end.
                ** add the '0' to all subsequences end-with-zero, the new subsequences will have at least 2 zero at end.

        else if the new charactor is '1':
            -- subsequences end-with-one has 3 cases:
                ** add the '1' to all subsequences end-with-one, the new subsequences will have at least 2 one at end
                ** add the '1' to all subsequences end-with-zero, the new subsequences will have 1 one at end and contain zero
                ** there is an extra subsequence '1' itself.
            -- subsequences end-with-zero: number is the same as before.
        '''
        has_zero = 0
        end_zero, end_one = 0, 0
        
        for v in binary:
            if v == '0':
                has_zero = 1
                end_zero = (end_zero + end_one) % (1e9 + 7)
            else:
                end_one = (end_zero + end_one + 1) % (1e9 + 7)
        
        return int((end_zero + end_one + has_zero) % (1e9 + 7))
```

# Oral:
Analysis the possible good subsequences, there are three different type subsequences:
```
    -- '0'
    -- starting with '1', end-with-zero
    -- starting with '1', end-with-one
```

With these 3 status, we can use dynamic programming to solve this problem.
Iterative over the binary string, if the new charactor is '0':
```
    -- it is sure there will be the subsequence '0'
    -- subsequences end-with-one: number is the same as before.
    -- subsequences end-with-zero has 2 cases:
        ** add the '0' to all subsequences end-with-one, the new subsequences will have 1 zero at end.
        ** add the '0' to all subsequences end-with-zero, the new subsequences will have at least 2 zero at end.

	So, end-with-zero = end-with-zero + end-with-one
	    end-with-one = end-with-one
	    has_zero = 1
```

Else if the new charactor is '1':
```
    -- subsequences end-with-one has 3 cases:
        ** add the '1' to all subsequences end-with-one, the new subsequences will have at least 2 one at end
        ** add the '1' to all subsequences end-with-zero, the new subsequences will have 1 one at end and contain zero
        ** there is an extra subsequence '1' itself.
    -- subsequences end-with-zero: number is the same as before.

     So, end-with-zero = end-with-zero
         end-with-one = end-with-one + end-with-zero + 1
```

The time complexity is: O(N).

The spatial complexity is: O(1)
