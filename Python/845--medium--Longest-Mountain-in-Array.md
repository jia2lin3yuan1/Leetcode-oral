#[845. Longest Mountain in Array](https://leetcode.com/problems/longest-mountain-in-array/description/)
+ `Medium`

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
```
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
```
Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

+ Example 1:

```
Input: arr = [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
```

+ Example 2:

```
Input: arr = [2,2,2]
Output: 0
Explanation: There is no mountain.
```
 

+ Constraints:

```
1 <= arr.length <= 104
0 <= arr[i] <= 104
```

# Solution:
```python {.line-numbers}
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ''' two pointer solution '''
        st, end = 0, -1
        max_length = 0
        for  k in range(1, len(arr)):
            if arr[k] == arr[k - 1]:
                st, end = k, -1
            elif arr[k] > arr[k - 1]:
                if end > 0: # end of a mountain and start a new trying
                    st, end = k - 1, -1
                else: # on the increasing slope, keep going
                    pass
            else:
                if k == st + 1: # if there is no increasing slope, it is not a mountain
                    st = k
                else: # find a mountain, update max_length
                    end = k
                    max_length = max((end - st + 1), max_length)
        return max_length


    def longestMountain_2(self, arr: List[int]) -> int:
        ''' state machine '''
        status, length = 0, 1 # status: 0 -- first element, 1 -- increasing, 2 -- decreasing
        max_length = 0
        for preV, v in zip(arr[:-1], arr[1:]):
            if v == preV:
                status, length = 0, 1
            elif v > preV:
                if status == 2:  # end of a mountain and start a new trying
                    status, length = 1, 2
                else: # on the increasing slope, keep going
                    status, length = 1, length + 1
            else:
                if status == 0: # if there is no increasing slope, it is not a mountain
                    status, length = 0, 1
                else:  # on decreasing slope, obtain a mountain, update max_length
                    status, length = 2, length + 1
                    max_length = max(max_length, length)

        return max_length
```

# Oral 1:
The problems about finding subarray in an array/list/str, and solving in one pass, we can always first try the  'two pointers' approach.

Define st and end to record the start and end of a subarray satisfying the condition. The length of the subarray would be end - st + 1
Iterate through the array, check the relation of the element and its previous element. We can tpdate st and end accordingly.

# Oral 2:
The problem can be solved using a state machine approach. If a subarray is a mountain, there are 3 possible status for each element: 0 -- the first element; 1 -- on the increasing slope; 2 -- on the decreasing slope.

Iterate over the whole array, comparing each element with its previous element, check what the new status can be.
