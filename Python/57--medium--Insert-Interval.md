#[57. Insert Interval](https://leetcode.com/problems/insert-interval/description/) 
+ `Medium`

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.


+ Example 1:

```
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

+ Example 2:

```
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
```


+ Constraints:

```
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
```

# Solution:
```python {.line-numbers}
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        mrg_st, ans = '#', []
        for k, ele in enumerate(intervals):
            # if the overlap starts
            if mrg_st == '#' and newInterval[0] <= ele[1]:
                mrg_st = min(ele[0], newInterval[0])
            
            # if need to stop the overlap
            if isinstance(mrg_st, int):
                if ele[0] > newInterval[1]: # stop before ele starts.
                    ans.append([mrg_st, newInterval[1]])
                    ans.append(ele)
                    mrg_st = '##'
                elif ele[1] >= newInterval[1]: # stop with ele[1]
                    ans.append([mrg_st, ele[1]])
                    mrg_st = '##'
                elif k == len(intervals) - 1: # stop with newInterval[1]
                    ans.append([mrg_st, newInterval[1]])
                    mrg_st = '##'
                else: # keep checking next ele.
                    pass
            else:
                # if need to insert newInterval ahead ele
                if mrg_st != '##' and newInterval[1] < ele[0]:
                    ans.append(newInterval)
                ans.append(ele)

        # if need to insert newInterval at the end
        if mrg_st != '##':
            ans.append(newInterval)

        return ans
```

# Oral:
To solve this problem, we need to analysis the relationship between one element from intervals and the newInterval.
1. first, we check if the overlap started by comparing the `newInterval[0]` and `ele[1]`.
2. if the overlap started, check if the overlap shold stop in `3` different cases.
    + `ele[0] > newInterval[1]`
    + `ele[1] >= newInterval[1]`
    + `ele[1] < newInterval[0]`, but it has reached the end of intervals.

3. If the overlap not started after judgement of `step 1`, then the ele should be added to new intervals. But remember to check if the newInterval should be insert before ele.
4. Use a flag to record the status of the overlap checking. If travesal of intervals is finished and newInterval is not inserted yet, append it to the end.

+ Given N is the number of elements in `intervals`
Time complexity: O(N)

Space complexity: O(N)
