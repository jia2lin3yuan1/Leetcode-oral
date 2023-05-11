#[1095. Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/description/) 
+ `Hard`

You may recall that an array arr is a mountain array if and only if:

```
arr.length >= 3
```

There exists some i with 0 < i < arr.length - 1 such that:
```
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
```
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.



+ Example 1:

```
Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
```

+ Example 2:

```
Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
```


+ Constraints:

```
3 <= mountain_arr.length() <= 104
0 <= target <= 109
0 <= mountain_arr.get(index) <= 109
```

# Solution:
```python {.line-numbers}
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak_idx = self.findPeak_binarySearch(0,
                                              mountain_arr.length()-1,
                                              mountain_arr)

        lft_find = self.binarySearch(target, 
                                     0, 
                                     peak_idx, 
                                     mountain_arr, 
                                     is_increase=True)
        if lft_find >= 0:
            return lft_find
        
        rht_find = self.binarySearch(target, 
                                    peak_idx, 
                                    mountain_arr.length()-1, 
                                    mountain_arr, 
                                    is_increase=False)
        return rht_find

    
    def findPeak_binarySearch(self, st, end, mountain_arr:'MountainArray') -> int:
        if st == end:
            return st
        elif st + 1 == end:
            return st if mountain_arr.get(st) > mountain_arr.get(end) else end

        mid = (st + end) //2
        if mountain_arr.get(mid) > mountain_arr.get(mid+1):
            return self.findPeak(st, mid, mountain_arr)
        else:
            return self.findPeak(mid, end, mountain_arr)
            
    
    def binarySearch(self, target, st, end, mountain_arr, is_increase=False):
        if st == end:
            return -1 if mountain_arr.get(st) != target else st
        elif  st > end:
            return -1

        mid = (st + end) // 2
        if mountain_arr.get(mid) == target:
            return mid
        elif mountain_arr.get(mid) > target:
            if is_increase:
                return self.binarySearch(target, st, mid-1, mountain_arr, is_increase)
            else:
                return self.binarySearch(target, mid+1, end, mountain_arr, is_increase)
        else:
            if is_increase:
                return self.binarySearch(target, mid+1, end, mountain_arr, is_increase)
            else:
                return self.binarySearch(target, st, mid-1, mountain_arr, is_increase)
```

# Oral:
As the mountain_arr can have length up to 10,000 and the submission of mountain_arr.get(k) is at most 100 times, the method should have time complexity in O(logN). For searching and this time complexity, we consider Binary Search.

The idea is to first find the Peak index in the mountain_arr. After that, we first perform the binary search on the left side of the mountain (including the peak), which is an increasing array. If target is not found, we then perform binary search on the right side (excluding the peak), which is a decreasing array.

To implement binary search for finding peak and target, we should carefully consider the edge cases and how to perform the recursive calling. 
